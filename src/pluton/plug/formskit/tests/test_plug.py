from mock import MagicMock

from pluton.application.testing import RequestCase

from ..plug import FormskitPlug


class TestFormskitPlug(RequestCase):
    _object_cls = FormskitPlug

    def madd_widget(self):
        return self.pobject(self.object().utils, 'add_widget')

    def test_add_raw_form(self):
        formcls = MagicMock()

        result = self.object().add_raw_form(formcls, 'arg', kw='kwarg')

        assert result == formcls.return_value
        formcls.assert_called_once_with(
            self.object(),
            'arg',
            kw='kwarg',
        )

    def test_add_form(self):
        formcls = MagicMock()
        widgetcls = MagicMock()
        madd_widget = self.madd_widget()

        result = self.object().add_form(
            formcls,
            'newname',
            widgetcls,
            'arg',
            kw='kwarg',
        )

        assert result == formcls.return_value
        formcls.assert_called_once_with(
            self.object(),
            'arg',
            kw='kwarg',
        )
        widgetcls.assert_called_once_with(result)
        madd_widget.assert_called_once_with('newname', widgetcls.return_value)

    def test_add_form_widget(self):
        widget = MagicMock()
        madd_widget = self.madd_widget()
        (left, right) = (MagicMock(), MagicMock())

        widget.from_form.return_value = (left, right)

        result = self.object().add_form_widget(
            widget,
            'newname',
            'arg',
            kw='kwarg',
        )

        assert result == left
        widget.from_form.assert_called_once_with(
            self.object(),
            'arg',
            kw='kwarg',
        )
        madd_widget.assert_called_once_with('newname', right)


