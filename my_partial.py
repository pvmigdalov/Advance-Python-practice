from functools import wraps


def my_partial(func, *p_args, **p_kwrags):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*p_args, *args, **p_kwrags, **kwargs)
    return wrapper

def foo(a, b, c=10, d=100):
    return (a + b) * c * d

p_foo = my_partial(foo, 1, c=1, d=1)
print(p_foo(5))


def my_partial_deco(*p_args, **p_kwrags):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*p_args, *args, **p_kwrags, **kwargs)
        return wrapper
    return decorator

@my_partial_deco(123, c=100, d=2)
def bar(a, b, c=10, d=100):
    return a + b + c + d

print(bar(0))