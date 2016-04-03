from yaml import load


class Routing(object):

    values_to_set = [
        'permission',
        'attr',
        'renderer',
        'http_cache',
        'wrapper',
        'decorator',
        'mapper',
        'context',
        'request_type',
        'request_method',
        'request_param',
        'match_param',
        'containment',
        'xhr',
        'accept',
        'header',
        'path_info',
        'check_csrf',
        'physical_path',
        'effective_principals',
        'custom_predicates',
        'predicates',
    ]

    def __init__(self, application):
        self.application = application

    @property
    def config(self):
        return self.application.config

    @property
    def paths(self):
        return self.application.paths

    def read_from_file(self, path):
        parser = RouteYamlParser(path)
        for route in parser.parse():
            self.add(**route)

    def read_from_dotted(self, path):
        self.read_from_file(
            self.paths.get_path_dotted(path)
        )

    def add(self, controller, route, url, *args, **kwargs):
        self.config.add_route(
            route,
            url,
            *args,
            **kwargs)

        self.add_view(controller, route_name=route)

    def add_view(self, controller, **kwargs):
        url = self._convert_url(controller)

        controller_class = self.config.maybe_dotted(url)

        for name in self.values_to_set:
            self.set_controller_config(kwargs, controller_class, name)

        self.config.add_view(url, **kwargs)

    def _convert_url(self, url):
        return url

    def set_controller_config(self, kwargs, controller, name):
        value = getattr(controller, name, None)
        if value:
            kwargs[name] = value

    def make(self):
        pass


class RouteYamlParser(object):

    def __init__(self, path):
        self.path = path

    def parse(self):
        self.read_yaml()
        yield from self._parse_route_yaml(self.data)

    def read_yaml(self):
        with open(self.path, 'r') as stream:
            self.data = load(stream)

    def _parse_route_yaml(self, data, prefix=''):
        for name, value in data.items():
            if type(value) is dict:
                yield from self._parse_route_yaml(value, prefix + name + '.')
            else:
                for element in value:
                    yield self._convert_route_dict(prefix + name, element)

    def _convert_route_dict(self, name, element):
        element['controller'] = name + '.' + element['controller']
        return element
