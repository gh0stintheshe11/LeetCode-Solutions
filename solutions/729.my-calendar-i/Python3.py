class MyCalendar:

    def __init__(self):
        # Initialize an empty list to store the booked events
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing bookings
        for s, e in self.bookings:
            if start < e and end > s:
                # There is an overlap
                return False
        # No overlap, add the new booking
        self.bookings.append((start, end))
        return True