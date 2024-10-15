from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h_sem = Semaphore(2)  # Allows 2 hydrogen threads to pass.
        self.o_sem = Semaphore(1)  # Allows 1 oxygen thread to pass.
        self.barrier = Barrier(3)  # Barrier for each full H2O molecule.

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()  # Wait for a spot to be available for H.
        self.barrier.wait()   # Wait for 3 threads in total (2 H + 1 O).
        releaseHydrogen()     # Release H.
        self.h_sem.release()  # Release the spot for another H thread.

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()  # Wait for a spot to be available for O.
        self.barrier.wait()   # Wait for 3 threads in total (2 H + 1 O).
        releaseOxygen()       # Release O.
        self.o_sem.release()  # Release the spot for another O thread.