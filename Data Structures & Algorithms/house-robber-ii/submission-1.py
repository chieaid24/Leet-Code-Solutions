class Solution:
    def rob(self, nums: List[int]) -> int:
        # similar to house robber 1, except now nums[0] is adjacent to nums[len(nums) - 1]
        # still, at each time, we can either pass, or steal. Update a memo array to the max amt
        # we can steal up until that index. 

        # however considering this, we can EITHER rob first OR rob last 
        # and the max robbed, we must find the maximum between these two situations -> how do we do this?
        # if we rob the first, then we can run our house robber functionality on the array not including
        # last index

        # then, if we rob the last, then we can run our functionality on the array not including index 0

        # therefore, we can STILL use the same function as our house robber 1 (memoization) but we have
        # 2 discrete cases that we can find the max between.

        # write our helper house robber 1 function
        def robSubArray(nums: List[int]) -> int:
            # we want to store an array with the maximum amt we can rob up to each point (
            # two cases, either we add the value (add it to n - 2's max) or skip the value (take n - 1's max))
            # then, we can update our current, and continue down the list of nums to get the end
            # or the max amt we can rob at that last index
            twoAway, oneAway = 0, 0 
            for n in nums:
                # get the max between our two cases, at this index
                temp = max(twoAway + n, oneAway)
                # now update our twoAway and oneAway for the next num
                twoAway = oneAway
                oneAway = temp
            return oneAway
        
        # main function, where we just call it twice with our two subarrays
        # check edge cases, one edge case that length == 1, such that its not even called into robSubArray
        if len(nums) == 1:
            return nums[0]

        return max(robSubArray(nums[:-1]), robSubArray(nums[1:]))


