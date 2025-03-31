"""  
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

(0,8),(8,10) is not conflict at 8

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""

from typing import (
    List,
)


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


"""
Definition of Interval:

"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        num_rooms = 0
        max_rooms = num_rooms

        s, e = 0, 0

        while s < len(start_times):
            # check if the current start time is more than the current end time
            # if it is, then that means that the previous meeting has ended and the current
            # meeting can be scheduled in an older room. If the current start time
            # is less than the current end time, then we need a new room

            if start_times[s] >= end_times[e]:
                # a meeting has to end before the next one starts, so we only increment e
                num_rooms -= 1
                e += 1
            else:
                s += 1
                num_rooms += 1

                max_rooms = max(max_rooms, num_rooms)

        return max_rooms
