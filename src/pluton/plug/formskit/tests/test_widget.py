from mock import MagicMock

from pluton.application.testing import RequestCase
from pluton.plug.testing.cache import cache

from ..widget import FormWidget


class ExampleFormWidget(FormWidget):
    form = MagicMock()


class TestFormWidget(RequestCase):

    _object_cls = FormWidget

    @cache
    def mform(self):
        return MagicMock()

    @cache
    def object(self):
        return super().object(self.mform())

    @cache
    def mrender_for(self):
        return self.pobject(self.object(), 'render_for')

    def test_get_tag_id(self):
        form = self.mform()
        form.get_name.return_value = 'myname'

        assert self.object().get_tag_id('tagname') == 'myname_tagname'

    def test_begin(self):
        form = self.mform()
        render_for = self.mrender_for()
        obj = self.object()

        obj.begin('tagid', 'mystyle', 'htmlclass')

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/begin.jinja2',
            {
                'action': form.action,
                'id': 'tagid',
                'name': form.get_name.return_value,
                'style': 'mystyle',
                'class': 'htmlclass',
                'enctype': None,
            }
        )

    def test_end(self):
        render_for = self.mrender_for()
        obj = self.object()

        obj.end()

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/end.jinja2',
            {
            }
        )

    def test_text(self):
        name = 'myname'
        field = MagicMock()
        form = self.mform()
        form.fields = {
            name: field,
        }
        render_for = self.mrender_for()
        obj = self.object()

        obj.text(name, disabled='disabled-val', autofocus='autofocus-val')

        field.get_name.assert_called_once_with()
        field.get_error_messages.assert_called_once_with()
        field.get_value_errors.assert_called_once_with(default=[])
        form.get_value.assert_called_once_with(name, default='')
        form.get_values.assert_called_once_with(name)

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/text.jinja2',
            {
                'name': field.get_name.return_value,
                'value': form.get_value.return_value,
                'values': form.get_values.return_value,
                'field': field,
                'templates': obj.Templates,
                'type': type,
                'str': str,
                'id': obj.get_tag_id(name),
                'label': field.label,
                'error': field.error,
                'messages': field.get_error_messages.return_value,
                'value_messages': field.get_value_errors.return_value,
                'disabled': 'disabled-val',
                'autofocus': 'autofocus-val',
            },
        )

    def test_file(self):
        name = 'myname'
        field = MagicMock()
        form = self.mform()
        form.fields = {
            name: field,
        }
        render_for = self.mrender_for()
        obj = self.object()

        obj.file(name, disabled='disabled-val', autofocus='autofocus-val')

        field.get_name.assert_called_once_with()
        field.get_error_messages.assert_called_once_with()
        field.get_value_errors.assert_called_once_with(default=[])
        form.get_value.assert_called_once_with(name, default='')
        form.get_values.assert_called_once_with(name)

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/file.jinja2',
            {
                'name': field.get_name.return_value,
                'value': form.get_value.return_value,
                'values': form.get_values.return_value,
                'field': field,
                'templates': obj.Templates,
                'type': type,
                'str': str,
                'id': obj.get_tag_id(name),
                'label': field.label,
                'error': field.error,
                'messages': field.get_error_messages.return_value,
                'value_messages': field.get_value_errors.return_value,
                'disabled': 'disabled-val',
                'autofocus': 'autofocus-val',
            },
        )

    def test_password(self):
        name = 'myname'
        field = MagicMock()
        form = self.mform()
        form.fields = {
            name: field,
        }
        render_for = self.mrender_for()
        obj = self.object()

        obj.password(name, disabled='disabled-val', autofocus='autofocus-val')

        field.get_name.assert_called_once_with()
        field.get_error_messages.assert_called_once_with()
        field.get_value_errors.assert_called_once_with(default=[])
        form.get_value.assert_called_once_with(name, default='')
        form.get_values.assert_called_once_with(name)

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/password.jinja2',
            {
                'name': field.get_name.return_value,
                'value': form.get_value.return_value,
                'values': form.get_values.return_value,
                'field': field,
                'templates': obj.Templates,
                'type': type,
                'str': str,
                'id': obj.get_tag_id(name),
                'label': field.label,
                'error': field.error,
                'messages': field.get_error_messages.return_value,
                'value_messages': field.get_value_errors.return_value,
                'disabled': 'disabled-val',
                'autofocus': 'autofocus-val',
            },
        )

    def test_select(self):
        name = 'myname'
        field = MagicMock()
        form = self.mform()
        form.fields = {
            name: field,
        }
        render_for = self.mrender_for()
        obj = self.object()

        obj.select(name, disabled='disabled-val', autofocus='autofocus-val')

        field.get_name.assert_called_once_with()
        field.get_error_messages.assert_called_once_with()
        field.get_value_errors.assert_called_once_with(default=[])
        form.get_value.assert_called_once_with(name, default='')
        form.get_values.assert_called_once_with(name)

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/select.jinja2',
            {
                'name': field.get_name.return_value,
                'value': form.get_value.return_value,
                'values': form.get_values.return_value,
                'field': field,
                'templates': obj.Templates,
                'type': type,
                'str': str,
                'id': obj.get_tag_id(name),
                'label': field.label,
                'error': field.error,
                'messages': field.get_error_messages.return_value,
                'value_messages': field.get_value_errors.return_value,
                'disabled': 'disabled-val',
                'autofocus': 'autofocus-val',
            },
        )

    def test_hidden(self):
        name = 'myname'
        field = MagicMock()
        form = self.mform()
        form.fields = {
            name: field,
        }
        render_for = self.mrender_for()
        obj = self.object()

        obj.hidden(name)

        field.get_name.assert_called_once_with()
        form.get_value.assert_called_once_with(name, default='')
        form.get_values.assert_called_once_with(name)

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/hidden.jinja2',
            {
                'name': field.get_name.return_value,
                'value': form.get_value.return_value,
                'values': form.get_values.return_value,
                'field': field,
                'templates': obj.Templates,
                'type': type,
                'str': str,
            },
        )

    def test_csrf_token(self):
        name = 'csrf_token'
        field = MagicMock()
        form = self.mform()
        form.fields = {
            name: field,
        }
        render_for = self.mrender_for()
        obj = self.object()

        obj.csrf_token()

        field.get_name.assert_called_once_with()
        form.get_value.assert_called_once_with(name, default='')
        form.get_values.assert_called_once_with(name)

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/hidden.jinja2',
            {
                'name': field.get_name.return_value,
                'value': form.get_value.return_value,
                'values': form.get_values.return_value,
                'field': field,
                'templates': obj.Templates,
                'type': type,
                'str': str,
            },
        )

    def test_submit(self):
        render_for = self.mrender_for()
        obj = self.object()

        obj.submit('mylabel', 'cls', 'base-cls')

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/submit.jinja2',
            {
                'label': 'mylabel',
                'class': 'cls',
                'base_class': 'base-cls',
            },
        )

    def test_form_error(self):
        form = self.mform()
        form.success = True
        render_for = self.mrender_for()
        obj = self.object()

        obj.form_error()

        form.get_error_messages.assert_called_once_with()

        render_for.assert_called_once_with(
            'pluton.plug.formskit:templates/form_error.jinja2',
            {
                'error': False,
                'messages': form.get_error_messages.return_value,
            },
        )

    def test_called_form(self):
        render_for = self.mrender_for()
        obj = self.object()
        obj.template = 'mytemplate'
        obj('a1', kw='kw1')

        render_for.assert_called_once_with(
            'mytemplate',
            {
                'args': ('a1',),
                'kwargs': {'kw': 'kw1'},
                'widget': obj,
            },
        )

    def test_from_form(self):
        parent = MagicMock()

        nform, nwidget = ExampleFormWidget.from_form(parent)

        assert nform == ExampleFormWidget.form.return_value
        assert isinstance(nwidget, FormWidget)
