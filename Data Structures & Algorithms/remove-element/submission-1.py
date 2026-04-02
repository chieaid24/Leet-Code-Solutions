class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # O(n^2)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)