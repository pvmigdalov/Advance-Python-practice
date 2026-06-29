import asyncio
from collections import defaultdict


context = defaultdict(int)


def coro_retry(*, n=0):
    if n < 0:
        n = 0

    def decorator(coro_func):
        async def coro_wrapper(*args, **kwargs):
            task = asyncio.current_task()
            task_name = task.get_name() if task else "Unknown"

            last_exc = None
            for i in range(n + 1):
                if i > 0:
                    print(f"Task {task_name} - retry {i}.")

                try:
                    return await coro_func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc

            if last_exc is not None:
                raise last_exc

        return coro_wrapper

    return decorator


@coro_retry(n=2)
async def test_coro():
    task = asyncio.current_task()
    context[task] += 1

    if context[task] < 3:
        raise ValueError("Oops")
    return True


async def main():
    return await asyncio.gather(
        test_coro(), test_coro(), test_coro(), return_exceptions=True
    )
    # return await asyncio.create_task(test_coro())


if __name__ == "__main__":
    print(asyncio.run(main()))
