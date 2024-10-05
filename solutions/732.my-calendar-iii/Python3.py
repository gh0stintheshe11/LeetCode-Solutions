class MyCalendarThree:

    def __init__(self):
        self.timeline = {}

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1

        ongoing = 0
        max_booking = 0
        for time in sorted(self.timeline):
            ongoing += self.timeline[time]
            if ongoing > max_booking:
                max_booking = ongoing

        return max_booking

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)