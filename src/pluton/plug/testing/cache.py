import sys
from functools import wraps

SESSION_CACHE = {}


class Cache(object):

    def __init__(self):
        pass

    def __contains__(self, item):
        return item in self.get_cache()

    def __getitem__(self, key):
        return self.get_cache()[key]

    def _create_cache_key(self, objself, args, kwargs):
        key = [self] + list(args) + sorted(kwargs.items())
        return self.fun.__name__ + str(key)

    def __call__(self, fun):
        self.fun = fun

        @wraps(fun)
        def wrapper(objself, *args, **kwargs):
            self.objself = objself
            cache_key = self._create_cache_key(objself, args, kwargs)
            cache = self.get_cache()
            return self._get_from_cache(cache, cache_key, objself, args, kwargs)
        return wrapper

    def _get_from_cache(self, cache, cache_key, objself, args, kwargs):
        cache = self.get_cache()
        if cache_key not in cache:
            cache[cache_key] = self. fun(objself, *args, **kwargs)

        return cache[cache_key]

    def get_cache(self):
        pass


class TestCache(Cache):

    def get_cache(self):
        try:
            return self.objself._test_cache
        except AttributeError:
            self.objself._test_cache = {}
            return self.objself._test_cache


class InstanceCache(Cache):

    def get_cache(self):
        try:
            return self.objself._instance_cache
        except AttributeError:
            self.objself._instance_cache = {}
            return self.objself._instance_cache


class ClassCache(Cache):

    def get_cache(self):
        cls = self.objself.__class__
        try:
            return cls._cls_cache
        except AttributeError:
            cls._cls_cache = {}
            return cls._cls_cache


class SessionCache(Cache):

    cache = {}

    def get_cache(self):
        return self.cache


def cache(method='test'):

    if hasattr(method, '__call__'):
        fun = method
        method = 'test'
    else:
        fun = None

    def choose_method(fun):
        name = fun.__name__

        def test(self, *args, **kwargs):
            key = [self] + list(args) + sorted(kwargs.items())
            cache_key = name + str(key)

            try:
                cache = self._instant_cache
            except AttributeError:
                cache = self._instant_cache = {}

            if cache_key not in cache:
                cache[cache_key] = fun(self, *args, **kwargs)

            return cache[cache_key]

        def instance(self, *args, **kwargs):
            key = list(args) + sorted(kwargs.items())
            cache_key = name + str(key)

            try:
                cache = self._instant_cache
            except AttributeError:
                cache = self._instant_cache = {}

            if cache_key not in cache:
                cache[cache_key] = fun(self, *args, **kwargs)
            return cache[cache_key]

        def cls(self, *args, **kwargs):
            key = list(args) + sorted(kwargs.items())
            cache_key = name + str(key)
            cls = self.__class__

            try:
                cache = cls._cls_cache
            except AttributeError:
                cache = cls._cls_cache = {}

            if cache_key not in cache:
                cache[cache_key] = fun(self, *args, **kwargs)
            return cache[cache_key]

        def module(self, *args, **kwargs):
            key = list(args) + sorted(kwargs.items())
            cache_key = name + str(key)

            module = sys.modules[self.__module__]
            cache = getattr(module, '_module_cache', {})
            setattr(module, '_module_cache', cache)
            if cache_key not in cache:
                cache[cache_key] = fun(self, *args, **kwargs)
            return cache[cache_key]

        def session(self, *args, **kwargs):
            key = list(args) + sorted(kwargs.items())
            cache_key = name + str(key)

            cache = SESSION_CACHE
            if cache_key not in cache:
                cache[cache_key] = fun(self, *args, **kwargs)
            return cache[cache_key]

        return locals()[method]

    if fun:
        return choose_method(fun)
    else:
        return choose_method
