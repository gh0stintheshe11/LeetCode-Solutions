from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        # Initializes a lock for each fork.
        self.forks = [Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        leftFork = philosopher
        rightFork = (philosopher + 1) % 5

        # Prevent deadlock by ensuring only four philosophers attempt to pick forks simultaneously.
        # Philosopher 0 tries to first pick the right fork, others first try to pick the left fork.
        if philosopher == 0:
            with self.forks[rightFork]:
                with self.forks[leftFork]:
                    pickRightFork()
                    pickLeftFork()
                    eat()
                    putLeftFork()
                    putRightFork()
        else:
            with self.forks[leftFork]:
                with self.forks[rightFork]:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putRightFork()
                    putLeftFork()