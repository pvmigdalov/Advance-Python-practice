from functools import partial


class my_classmethod:
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, owner):
        return partial(self._func, owner)
    

class Test:
    @my_classmethod
    def foo(cls, a, b):
        print(cls.__name__)
        print(f"{a=}, {b=}")

Test.foo(1, 2)
Test().foo(3, 4)    