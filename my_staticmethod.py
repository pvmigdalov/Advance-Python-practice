class my_staticmethod:
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, owner):
        return self._func
    

class Test:
    @my_staticmethod
    def foo(a, b):
        print(f"{a=}, {b=}")

Test.foo(1, 2)
Test().foo(3, 4)
