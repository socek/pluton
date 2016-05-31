from formskit import Form
from mock import MagicMock

from pluton.application.testing import RequestCase
from pluton.plug.testing.cache import cache

from ..models import CsrfMustMatch
from ..models import PostForm


class MockedPostForm(Form):

    @property
    @cache('instance')
    def reset(self):
        return MagicMock()

    @property
    @cache('instance')
    def validate(self):
        return MagicMock()


class ExamplePostForm(PostForm, MockedPostForm):

    def _get_request_cls(self):
        return lambda x: x


class ExamplePostFormWithoutCsrf(PostForm, MockedPostForm):
    with_csrf = False


class ExamplePostFormWithAlwaysSubmitting(PostForm, MockedPostForm):
    always_submitting = True


class TestFlashMessageController(RequestCase):

    _object_cls = ExamplePostForm

    @cache
    def object(self):
        return super().object(self.mrequest())

    @cache
    def madd_form_validator(self):
        return self.pobject(PostForm, 'add_form_validator')

    @cache
    def minit_csrf(self):
        return self.pobject(PostForm, 'init_csrf')

    @cache
    def mcsrf_must_match(self):
        return self.patch('pluton.plug.formskit.models.CsrfMustMatch')

    def test_init(self):
        add_form_validator = self.madd_form_validator()
        init_csrf = self.minit_csrf()
        csrf_must_match = self.mcsrf_must_match()

        self.object()

        add_form_validator.assert_called_once_with(
            csrf_must_match.return_value)
        init_csrf.assert_called_once_with()

    def test_reset(self):
        self.mregistry()
        obj = self.object()
        init_csrf = self.minit_csrf()
        super(PostForm, obj).reset.reset_mock()

        obj.reset()

        super(PostForm, obj).reset.assert_called_once_with()

        init_csrf.assert_called_once_with()

    def test_validate(self):
        post = self.m_post()
        obj = self.object()

        result = obj.validate()

        assert result == super(PostForm, obj).validate.return_value
        post.dict_of_lists.assert_called_once_with
        super(PostForm, obj).validate.assert_called_once_with(
            post.dict_of_lists.return_value
        )

    def test_without_csrf(self):
        parent = self.mrequest()
        form = ExamplePostFormWithoutCsrf(parent)
        assert form.form_validators == []

        form.reset()
        assert form.fields == {}

    def test_always_submitted(self):
        parent = self.mrequest()
        form = ExamplePostFormWithAlwaysSubmitting(parent)
        assert form._is_form_submitted({}) is True

        form.always_submitting = False
        assert form._is_form_submitted({}) is False

        data = {
            form.form_name_value: [form.get_name(), ],
        }
        assert form._is_form_submitted(data) is True


class TestCsrfMustMatch(RequestCase):

    _object_cls = CsrfMustMatch

    @cache
    def mform(self):
        obj = MagicMock()
        obj.POST = self.m_post()
        return obj

    @cache
    def object(self):
        obj = self._object_cls()
        obj.set_form(self.mform())
        return obj

    @cache
    def mcheck_csrf_token(self):
        return self.patch('pluton.plug.formskit.models.check_csrf_token')

    def test_validate(self):
        post = self.m_post()
        form = self.mform()
        check_csrf_token = self.mcheck_csrf_token()
        obj = self.object()

        assert obj.validate() == check_csrf_token.return_value

        assert post['csrf_token'] == form.get_value.return_value
        form.get_value.assert_called_once_with('csrf_token')
        check_csrf_token.assert_called_once_with(form.request, raises=False)
