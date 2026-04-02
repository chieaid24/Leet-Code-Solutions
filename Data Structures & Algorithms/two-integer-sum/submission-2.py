class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict of "seen" values (key->value, value->index)
        # loop through the array checking the set for the complement
        # if reach end return false
        seen = {}
        for k in range(len(nums)):
            if target - nums[k] in seen.keys():
                return [seen[target - nums[k]], k]
            seen[nums[k]] = k