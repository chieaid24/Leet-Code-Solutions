class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force is to find every subarray of the array, (o(n^2) time)
        # Checking its product, then returning the max.

        # Optimizations:
        # Sliding window, where we start both pointers at the left, increase window size
        # if new product is >, else decrease window size
        # Doesn't work with [-2 -1 -2 -1]

        # DP Solution such that it tracks the max product up until this index (break into subproblems)
        # At each index, we can either multiply by the last max, or just take the index by itself
        # Need an extra logic step for a negative value (as our example above)
        # Brute force check if the current i in -, then check if NEXT index is negative, if so then keep
        # the largest magnitude - num
        # Idea: if we a store a tuple at every index, where 0 is the maxPos and 1 is maxNeg then at each
        # step, if it is negative, we look at maxNeg, and if it is +, then we look at maxPos. We always update
        # both however, and when taking the last index, we can just take maxPos. 
        # This way, if something like [-100 2 1 -100] happens, it will still be correct, as the - will be 
        # carried throughout
        maxWin, minWin = 1, 1
        maxTot = float("-inf")
        for num in nums:
            tempMax = max(num, num * maxWin, num * minWin)
            minWin = min(num, num * maxWin, num * minWin)
            maxWin = tempMax
            maxTot = max(maxTot, maxWin)
        return maxTot

        # max = -4, min = 1, maxTot = -inf
        # [-4,-3,-2]
