from pluton.plug.formskit.models import PostForm

from .plugs import PluggedMixin


class Form(PluggedMixin, PostForm):
    pass
