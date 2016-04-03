from decorator import decorator


def deco(func):
    def wrapper(func, *args, **kwargs):
        with ContextManager as something:
            return func(*args, something, **kwargs)

    return decorator(wrapper, func)


class TestSomething(object):

    @deco
    def elo(self, something):
        pass
