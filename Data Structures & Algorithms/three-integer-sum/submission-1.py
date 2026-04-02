class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # since we can't have duplicate triplets, always want to 
        # ignore duplicate numbers, since after you evaluate a number, 
        # a duplicate will create an extra solution that you don't want
        # handle this by looping through the sorted array, and 
        # checking if the last value was equal to current value, if so
        # continue

        # Brute force:
        # cannot just triple loop through it initially, as if there are
        # duplicate values -> result in duplicate triples
        #
        # sort the array (group the duplicates together), then as you 
        # step through it, check if duplicate values and continue

        # Better solution:
        # a single loop is needed as the first value being compared,
        # however, we know that to = 0, the second two values must =-first
        # use a two-sum strategy to find this (hash set, or sort + two pointers)
        # since the array is already sorted, let's use two pointers

        # Time: O(nlogn) <sorting> + O(n^2) <first loop plus two pointers 2sum (O(n))
        
        


        # 1. sort the array
        nums.sort()
        # [-1, -1, -1, 0, 1, 2]
        # [-4, -3, -3, -1, 0, 1, 3, 3]
        # [0, 0, 0, 0, 0]

        # 1.5. Initialize res
        res = []

        # 2. loop through the array once, and then nest a 2sum two pointers solution (can be multiple solutions)
        # if you find a solution, force step inward from both 
        for a in range(len(nums) - 2):
            # as you loop through, skip duplicate values (they've already been evaluated)
            if a and nums[a] == nums[a - 1]: # in Python 0 is falsy -> when index = 0, short circuit
                continue
            
            # 2sum with two pointers, sum being -nums[a]
            target = -nums[a]
            l = a + 1
            r = len(nums) - 1
            while (r > l):
                currSum = nums[l] + nums[r]
                if currSum == target:
                    # found a triplet
                    triplet = [nums[a], nums[l], nums[r]]
                    res.append(triplet) # use .append() to create a list of lists
                    # increment left ptr until it reaches a new value
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    # could potentially decrement the right pointer until
                    # a different value -> will result in this anyway
                else:
                    if currSum > target:
                        # decr right ptr until diff value
                        r -= 1

                    elif currSum < target:
                        # inc left ptr
                        l += 1
        return res

                    

                     