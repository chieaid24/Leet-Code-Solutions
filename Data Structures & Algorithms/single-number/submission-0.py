class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # intuition here is use XOR since we know that a number xor itself = 0, but a number xor 0 is 
        # a number. This means if we XOR ever number with 0, then we will be left with the 
        # missing number
        res = 0
        for num in nums:
            res = num ^ res
        return res