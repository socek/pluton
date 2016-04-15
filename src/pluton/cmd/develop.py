from bael.project.develop import Develop


class PlutonDevelop(Develop):

    def phase_settings(self):
        super().phase_settings()
        self.settings['ignore_inits_dirs'].append('templates')
        self.settings['ignore_inits_dirs'].append('static')
