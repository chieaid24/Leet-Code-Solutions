"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # loop through intervals, checking if the next start time is before the last end time
        # this only works if intervals are sorted by time?
        # real! just sort it first using a small lambda function

        #sort intervals
        intervals.sort(key=lambda i: i.start)

        for k in range(1, len(intervals)):
            first = intervals[k - 1]
            second = intervals[k]

            # check if the second start time is before the first end time
            if second.start < first.end:
                return False
        return True