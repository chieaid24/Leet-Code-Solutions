class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set, then loop through the array checking if it is the beginning of a sequence
        # ie it has not left neighbor -> the way to check whether to start counting from this entry
        # O(n) since each number is checked twice max

        numSet = set(nums)
        currMax = 0
        # loop through the nums, checking if it is the potential start of a sequence
        for num in nums:
            if not num - 1 in numSet:
                # this is the beginning of a sequence
                tempMax = 1
                temp = num
                while temp + 1 in numSet:
                    tempMax += 1
                    temp += 1
                currMax = max(currMax, tempMax)
        return currMax
