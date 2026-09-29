from functools import wraps
from typing import Any, Callable


def retry_on_exception(retries: int):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            try:
                result = func(*args, **kwargs)
                print("ok")
                return result
            except Exception as ex:
                if wrapper._retries < retries:
                    wrapper._retries += 1
                    print(ex.__class__.__name__)
                    return wrapper(*args, **kwargs)
                elif wrapper._retries == retries:
                    print("final ", ex.__class__.__name__)

        wrapper._retries = 0
        return wrapper

    return decorator


error_counter_success = 0


@retry_on_exception(retries=3)
def test_success_after_one_fail():
    global error_counter_success
    if error_counter_success < 2:
        error_counter_success += 1

        raise ValueError
    return "Success after fail!"


test_success_after_one_fail()
