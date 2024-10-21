from threading import Lock

class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock1.acquire()
        self.lock2 = Lock()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        printSecond()
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        printThird()