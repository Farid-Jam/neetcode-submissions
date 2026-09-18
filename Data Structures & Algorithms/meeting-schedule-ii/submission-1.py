"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for event in intervals:
            events.append([event.start, 1])
            events.append([event.end, -1])
        
        events.sort()

        total = 0
        curr = 0
        
        for event in events:
            curr += event[1]
            total = max(total, curr)
        
        return total