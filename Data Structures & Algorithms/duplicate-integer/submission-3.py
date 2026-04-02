class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through array once, adding values to a set, if 
        # the value ever appears in the set return true, else return false
        seen = set()
        for k in range(len(nums)):
            if nums[k] in seen:
                return True
            seen.add(nums[k])
        return False
