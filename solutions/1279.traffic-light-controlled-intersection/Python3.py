from threading import Lock

class TrafficLight:
    def __init__(self):
        # 0 for Road A, 1 for Road B
        self.currentGreen = 0
        self.lock = Lock()
    
    def carArrived(
        self,
        carId: int,
        roadId: int,
        direction: int,
        turnGreen: 'Callable[[], None]',
        crossCar: 'Callable[[], None]'
    ) -> None:
        with self.lock:
            if (roadId == 1 and self.currentGreen == 1) or (roadId == 2 and self.currentGreen == 0):
                turnGreen()
                self.currentGreen = 1 if roadId == 2 else 0
            
            crossCar()