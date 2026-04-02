class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # first pass: 
        # sort the nums, loop from 0 to nums.length, check if index val = nums[index] 
        nums.sort()
        for k in range(len(nums)):
            if k != nums[k]:
                return k
        return len(nums)