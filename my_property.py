class my_property:
    def __init__(self, getter):
        self._getter = getter
        self._setter = None
        self._deletter = None


    def __get__(self, instance, owner):
        return self._getter(instance)
    
    def __set__(self, instance, value):
        if not self._setter:
            raise NotImplementedError("Method setter not implemented")
        self._setter(instance, value)

    def __delete__(self, instance):
        if not self._deletter:
            raise NotImplementedError("Method deletter not implemented")
        self._deletter(instance)    

    def setter(self, func):
        self._setter = func
        return self
    
    def deletter(self, func):
        self._deletter = func
        return self


class Test:
    def __init__(self):
        self._foo = 1

    @my_property
    def foo(self):
        print("Call property foo (getter)")
        return self._foo
    
    @foo.setter
    def foo(self, value):
        print("Call property foo (setter)")
        self._foo = value

    @foo.deletter
    def foo(self):
        print("Call property foo (deletter)")


t = Test()
print(t.foo)

t.foo = 100
print(t.foo)

del t.foo
