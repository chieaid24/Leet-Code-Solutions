class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointers approach, one on each end of the array.
        # Track the current max, then increment the "shorter" end
        # Go until the pointers are equal
        l, r = 0, len(heights) - 1
        currMax = 0
        while l < r:
            # calc volume
            volume = (r - l) * min(heights[r], heights[l])
            # update max
            currMax = max(volume, currMax)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return currMax