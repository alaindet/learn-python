from contextlib import contextmanager
from time import perf_counter, sleep

class Timer:

    name: str
    timing: int = 0
    _started_on: int = 0

    def __init__(self, name: str):
        self.name = name
        self.start()

    def start(self) -> None:
        self._started_on = perf_counter()

    def stop(self) -> None:
        self.timing = perf_counter() - self._started_on

    def to_string(self) -> str:
        if self._started_on == 0:
            return f'Timer "{self.name}": not started yet'

        return f'Timer "{self.name}": {self.timing} seconds'

class TimerContext:

    total_seconds: int = 0

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(f'Total: {self.total_seconds} seconds')

    @contextmanager
    def timer(self, name: str):
        timer = Timer(name)
        timer.start()
        yield
        timer.stop()
        self.total_seconds += timer.timing
        print(timer.to_string())

if __name__ == '__main__':
    with TimerContext() as ctx:
        for i in range(10):
            name = f'Operation #{i}'
            with ctx.timer(name):
                sleep(0.2)