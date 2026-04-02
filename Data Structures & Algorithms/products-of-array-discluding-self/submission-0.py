class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # want to get the prefix value * the postfix value
        # where the prefix value is all of the values before the number multiplied together
        # and the postfix value is all of the values after the number multiplied together
        # default values for post + prefix are 1, multiply by the indexes as they go across
        
        # could also create a prefix array, a postfix array, then multiply the two to get the final array
        
        # when calculating the prefix values, store the prefix value in the actual value of an array
        # then when looping through for the postfixes, multiply each post fix at each value

        # create the blank solution array
        res = [1] * len(nums)

        # loop through and add the prefix values for each value in nums
        # track the current prefix (just multiplying each of the entries as you go along)
        prefix = 1
        for k in range(len(nums)):
            res[k] = prefix
            prefix *= nums[k]

        # do the same for the postfix values:
        #   step through it backwards, postfix initially is 1, multiply by the value, then multiply that by the prefix
        postfix = 1
        for k in range(len(nums) - 1, -1, -1):
            res[k] *= postfix
            postfix *= nums[k]
        return res