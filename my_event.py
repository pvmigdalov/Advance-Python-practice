import asyncio
import contextlib


class MyEvent:
    def __init__(self):
        self._loop = asyncio.get_running_loop()
        self._done = False
        self._future = self._loop.create_future()
        
    async def wait(self, *, timeout: float | None = None) -> bool:
        with contextlib.suppress(asyncio.TimeoutError):
            async with asyncio.timeout(timeout):
                self._done = await self._future
        return self.is_set()
    
    def set(self):
        if not self._future.done():
            self._future.set_result(True)
    
    def is_set(self):
        return self._done
    
    def clear(self):
        if not self._future.done():
            self._future = self._loop.create_future()
        self._done = False
        

async def coro(msg, event, timeout=None):
    await event.wait(timeout=timeout)
    print(msg)
    
async def event_handle(event):
    print("set event in 2 seconds")
    await asyncio.sleep(2)
    event.set()
    
async def main():
    event = MyEvent()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coro("task-1", event))
        tg.create_task(coro("task-2", event))
        tg.create_task(event_handle(event))
        
    print("reuse event")
    event.clear()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coro("task-1", event, 1))
        tg.create_task(coro("task-2", event, 1))
        tg.create_task(event_handle(event))
        

if __name__ == "__main__":
    asyncio.run(main())

