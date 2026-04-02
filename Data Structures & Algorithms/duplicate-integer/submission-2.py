class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set (cannot contain repeat values)
        seen_set = set()
        # loop through the list and check if each int is already in the set
        for num in nums:
            if num in seen_set:
                return True;
        # if so, return True, if not, add it to the set
            seen_set.add(num)
        return False
        # if loop exits, return False