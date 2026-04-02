class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # lets just sort by the x[0] value, and then have a separate function where we can merge
        # the two lists, then continue iterating through the list
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # if the start of the new interval is before or equal to the end of the last, then overlapping
            if start <= lastEnd:
                # calculate the new ned
                output[-1][1] = max(output[-1][1], end)
            else:
                # append it to output
                output.append([start, end])
        return output