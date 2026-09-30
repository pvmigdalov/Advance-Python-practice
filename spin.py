import asyncio
from contextlib import suppress
from itertools import cycle
from typing import Any


async def spin(msg: str, done: asyncio.Event):
    smiles = [
        "\U0001f4a9",
        "\U0001f921",
        "\U0001f479",
        "\U0001f47a",
        "\U0001f47b",
        "\U0001f47d",
        "\U0001f47e",
        "\U0001f916",
    ]

    # for char in cycle("\|/-"):
    for char in cycle(smiles):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        with suppress(asyncio.TimeoutError):
            await asyncio.wait_for(done.wait(), timeout=0.6)
            break

    blancks = " " * len(status)
    print(f"\r{blancks}", end="\r", flush=True)
    # print("\r", end="", flush=True)


async def slow(duration: float = 3) -> int:
    await asyncio.sleep(duration)
    return 42


async def supervisor(task: asyncio.Task, done: asyncio.Event) -> Any:
    result = await task
    done.set()
    return result


async def main():
    print("Start calculating...")
    await asyncio.sleep(1)

    done = asyncio.Event()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(spin("thinking!", done))
        supervisor_task = tg.create_task(supervisor(tg.create_task(slow(5)), done))

    result = supervisor_task.result()
    print(f"Answer: {result}")


if __name__ == "__main__":
    asyncio.run(main())
