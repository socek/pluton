from pluton.application.widget import SingleWidget


class BreadCrumbWidget(SingleWidget):
    renderer = 'pluton.breadcrumbs:templates/widgets/breadcrumb.haml'

    def __init__(self, breadcrumb):
        super().__init__()
        self.breadcrumbs = breadcrumb

    def make(self):
        self.context['breadcrumbs'] = self.breadcrumbs
