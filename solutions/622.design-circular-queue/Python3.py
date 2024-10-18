class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # Initialize the queue with a fixed size
        self.max_size = k  # Maximum size of the queue
        self.front = 0  # Pointer to the front of the queue
        self.rear = -1  # Pointer to the rear of the queue
        self.size = 0  # Current size of the queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size  # Move rear pointer to the next position
        self.queue[self.rear] = value  # Insert the new value
        self.size += 1  # Increase the size of the queue
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size  # Move front pointer to the next position
        self.size -= 1  # Decrease the size of the queue
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]  # Return the front element

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]  # Return the rear element

    def isEmpty(self) -> bool:
        return self.size == 0  # Check if the queue is empty

    def isFull(self) -> bool:
        return self.size == self.max_size  # Check if the queue is full
