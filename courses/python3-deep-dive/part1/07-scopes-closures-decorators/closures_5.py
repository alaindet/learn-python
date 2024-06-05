from time import sleep, perf_counter


class TimerClass:

    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start


timer1 = TimerClass()
sleep(0.5)
print(timer1())


def timerClosure():
    start = perf_counter()

    def stopwatch():
        return perf_counter() - start

    return stopwatch


timer2 = timerClosure()
sleep(0.5)
print(timer2())
