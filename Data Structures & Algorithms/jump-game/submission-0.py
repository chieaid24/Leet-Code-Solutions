class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # BF: for every index, decision tree of n decisions, where we jump that amount and then
        # continue recursively until one of the decisions ends up being true
        # O(m^n) where m is the size of the n in nums, and n is the length of nums
        #
        # If we start from jumping the MAX then decrementing the amt we jump by every fail, this is a 
        # greedy solution, that is the same time complexity as above, but average case probably will be
        # faster (since we make less the least jumps possible as we're jumping the furthest we can)

        # Test some bottom up DP solution. Cache of size n, start from the end
        # the last index = True (we can get there). Now we step backwards, see if dp[i + nums[i]] is true
        # if so, then we know dp[i] is true. Else, we can see if dp[i + nums[i]--] is true (until nums[i] < 1)
        # and continue until we find a true OR nums[i] < 1, in that case we move on.
        # This is basically the same time complexity as the first one? NO! Because we are caching the 
        # values? instead of going down the same decision trees many times, when we work bottom up, we can 
        # cache our previously calculated values, so we don't have to recalculate "if we can get to last
        # starting from index 4" or whatever. Also if the initial jump is ever out of bounds, we know it
        # will be true (possible to get to the end) -> so we don't have to keep decrementing and checking.
        # Time complexity O(n * m) space is O(n)

        cache = [False] * len(nums)
        cache[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            while jump > 0:
                if (i + jump) >= len(cache) or cache[i + jump]:
                    cache[i] = True
                    break
                else:
                    jump -= 1
        return cache[0]
        # jump = 1
        # [1 2 1 0 1]
        # [0 0 0 0 1]