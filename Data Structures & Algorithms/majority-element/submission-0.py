class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # with o(n) space have a dict counting, and every time we increment, check it against the length
        # of the list
        
        # since we know a majority exists, pick a candidate at the beginning, and then
        # increment it if the next value is equal, else decrement it
        # at the end of the list, our candidate will be the majority
        res = 0
        count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res