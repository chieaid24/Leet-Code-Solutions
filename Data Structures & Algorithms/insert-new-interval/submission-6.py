class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # We have some cases as we check each pair starting from the beginning:
        # 1) start is before the start of new AND end is before the start of new -> continue
        # 2) start is before the start of new and end is after (or equal) to start of new -> need to merge
        # We then merge, creating a new interval such that the end is the max between old and new end
        # After this merge, we must check the next index, and see if we have to merge again (max 2 merges)
        # (Same logic as above)

        # Once we do this once, we can exit
        # This is an O(n) solution since we maximum check every pair until we find where to merge
        # However! We can't just loop once, we have to check EVERY other pair in the list, in case
        # we need to merge them (this is because there is a case such that the newInterval overlaps
        # with many intervals!!)
        # Therefore, we just iterate through the intervals, add them to our res list if our new
        # comes after, then when we merge, we keep merging, and only after the next ones are good, then
        # we can append them to our res list
        
        # edge case len(intervals) == 0
        res = []
        start, end = newInterval[0], newInterval[1]
        merged = False
        i = 0
        while i < len(intervals):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if end < curr_start:
                merged = True
                res.append([start, end])
                res.extend(intervals[i:])
                break
            elif start > curr_end:
                res.append(intervals[i])
            else: # we merge
                start = min(start, curr_start)
                end = max(end, curr_end)
            i += 1
        if not merged:
            res.append([start, end])
        return res

        # res = [[1 5] [9 10]]
        # start = 0, end = 1
        # i = 0
        # merged = 0
        # curr_start = 2, curr_end = 3
        # [[2,3],[4,5]]
        # [[0 1] [2 3] [4 5]]
