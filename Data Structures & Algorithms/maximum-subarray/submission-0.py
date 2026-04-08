class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force: just check every subsequence, check its sum + find the max
        # this is a O(n^2) time solution!

        # better solution:
        # two pointer approach, both starting at index 0. 
        # increment the right pointer, add it to the sum
        # If the new value + currSum < 0, then continue both pointers to r + 1
        # else, then append it on.
        # Constantly keep track of the max, return it when the pointers reach the end
        # time: O(n) evaluates each value a max of 1 time
        # space: O(1), just tracks constants

        i = 0
        max_sum, curr_sum = float("-inf"), 0

        while i < len(nums):
            # check our condition!
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                # "reset" starting from r + 1
                curr_sum = 0
            i += 1
        
        return max_sum
        # max = -1 , curr = -1
        # [2 -3 4 -2 2 1 -1 4]
        
        # other edge cases
        # [-8 -2 -1]