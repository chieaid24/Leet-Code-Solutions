class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # DFS and keep track of i to determine which nums it can use it said branch

        def dfs(total, i) -> int:
            # base case
            if i == len(nums):
                return total
            # recursive case where we add the total if we include i and total if we don't include i
            return dfs(total ^ nums[i], i + 1) + dfs(total, i + 1)
        
        return dfs(0, 0)
