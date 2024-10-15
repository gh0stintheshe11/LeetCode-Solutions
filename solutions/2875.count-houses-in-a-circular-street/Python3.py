class Solution:
    def houseCount(self, street: 'Street', k: int) -> int:
        # Close all doors while counting to ensure starting point
        for _ in range(k):
            if street.isDoorOpen():
                street.closeDoor()
            street.moveRight()

        # Start from initial position (all doors closed)
        street.openDoor()  # Mark starting house
        count = 1
        street.moveRight()  # Move to the next house

        # Move right until we find the marked house again
        while not street.isDoorOpen():
            count += 1
            street.moveRight()

        return count