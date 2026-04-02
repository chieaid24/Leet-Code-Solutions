class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # you can brute force it by having nested for loop that for each
        # value, adds to all other values and checks

        # or you can transfer data to a hashmap (dict) with key -> number, value -> index)
        # then loop through the list and check if its complement exits in hashmap
        # o(n)

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for k in range(len(nums)):
            complement = target - nums[k]
            if complement in hashmap and hashmap[complement] != k:
                # found it!
                return [k, hashmap[complement]] 
        return 0