"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        for event in intervals:
            events.append([event.start, 1])
            events.append([event.end, -1])
        
        events.sort()

        total = 0
        for event in events:
            total += event[1]
            if total >= 2:
                return False
        
        return True