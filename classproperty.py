class classproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(owner)


if __name__ == "__main__":

    class Test:
        _foo = 123

        @classproperty
        def foo(cls):
            return cls._foo + 100

    print(Test.foo)
