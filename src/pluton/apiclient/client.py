from requests import post

from .checks.disk import disk_space_check


class ApiClient(object):
    main_url = 'http://127.0.0.1:6543/api'

    urls = {
        'event:add': '/event/add',
    }

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _call(self, name, data):
        url = self.main_url + self.urls[name]
        data['api_key'] = self.api_key
        data['api_secret'] = self.api_secret
        return post(
            url,
            data,
        )

    def add_event(self, name, state, raw, arg=None, **kwargs):
        data = {
            'form_name': 'AddEventForm',
            'name': name,
            'state': state,
            'arg': arg,
        }
        for key, value in raw.items():
            data['raw_' + key] = value
        data.update(kwargs)
        return self._call('event:add', data)

    def send_disk_chack(self, disk):
        raw = disk_space_check(disk)
        name = 'Disk check'
        self.add_event(name, 'normal', raw, arg=disk)
