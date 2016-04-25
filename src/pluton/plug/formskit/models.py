from pyramid.session import check_csrf_token

from formskit import Form
from formskit.formvalidators import FormValidator
from pluton.plug.plug import RequestPlug


class PostForm(Form, RequestPlug):
    with_csrf = True
    always_submitting = False

    def __init__(self, parent):
        self.feed_parent(parent)
        super().__init__()

        if self.with_csrf:
            self.add_form_validator(CsrfMustMatch())

    def reset(self):
        super().reset()
        self.init_csrf()

    def init_csrf(self):
        if self.with_csrf:
            self.add_field('csrf_token')
            self.set_value('csrf_token', self.request.session.get_csrf_token())

    def validate(self):
        return super().validate(self._get_form_data())

    def _get_form_data(self):
        return self.POST.dict_of_lists()

    def _is_form_submitted(self, raw_data):
        return self.always_submitting or super()._is_form_submitted(raw_data)


class CsrfMustMatch(FormValidator):

    message = "CSRF token do not match!"

    def validate(self):
        self.form.POST['csrf_token'] = self.form.get_value('csrf_token')
        return check_csrf_token(self.form.request, raises=False)
