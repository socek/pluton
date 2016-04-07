
from pluton.plug.formskit.models import PostForm
from pluton.plug.formskit.widget import FormWidget

from pluton.application.controller import Controller
from pluton.application.controller import JsonController


class MyPostForm(PostForm):

    def create_form(self):
        self.add_field('name', label='Nazwa')


class MyPostFormWidget(FormWidget):
    template = 'pluton.dashboard:templates/form.haml'
    form = MyPostForm


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.haml'

    def make(self):
        self.context['ctrl'] = 'one'
        self.context['clients'] = self.clients.find_all()
        self.context['ses'] = self.request.session.get('ses', 0)
        self.context['ses'] += 1
        self.request.session['ses'] = self.context['ses']

        form = self.forms.add_form_widget(MyPostFormWidget)

        if form.validate():
            print('ok')


class DashboardSecond(JsonController):

    def make(self):
        self.context['ctrl'] = 'two'
