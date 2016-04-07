from fanstatic import Fanstatic

from pluton.plug.application import Application


class FanstaticApplication(Application):

    def _return_wsgi_app(self):
        return Fanstatic(
            super()._return_wsgi_app(),
            **self.settings['fanstatic']
        )
