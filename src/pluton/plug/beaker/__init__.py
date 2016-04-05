from pluton.plug.app_plug import AppPlug


class BeakerAppPlug(AppPlug):

    def create_config(self):
        self.parent.config.include('pyramid_beaker')
