class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_map = {}
        for num in nums:
            if value_map.get(num) is None:
                value_map[num] = 1
            else:
                return True
        return False
        