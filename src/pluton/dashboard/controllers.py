from pluton.plug.controller import Controller
from pluton.plug.controller import JsonController
from pluton.dashboard.driver import ClientDriver
from pluton.plug.formskit.plug import FormskitPlug
from pluton.plug.formskit.models import PostForm
from pluton.plug.formskit.widget import FormWidget


class MyPostForm(PostForm):

    def create_form(self):
        self.add_field('name', label='Nazwa')


class MyPostFormWidget(FormWidget):
    template = 'pluton.dashboard:templates/form.haml'
    form = MyPostForm


class Dashboard(Controller):
    renderer = 'pluton.dashboard:templates/dashboard.haml'

    def create_plugs(self):
        super().create_plugs()
        self.clients = self.add_plug(ClientDriver)
        self.forms = self.add_plug(FormskitPlug)

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
