class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # solution here is a decision tree, such that we want to avoid any repeats.
        # we can do this by using a binary tree, where one branch is using said number
        # then other branch you cannot use that number in that spot again
        # Doing this, we can look at every combination, without repeating at any point during the 
        # iteration
        # use a DFS recursive function such that we have to track the index that
        # we are able to use in nums, and need the current list of solution, and need
        # the total that is added together, so we can calculate target
        res = []

        def dfs(i, currList, total):
            # base cases
            if total == target:
                res.append(currList.copy())
                return
            if total > target or i >= len(nums):
                return
            
            # recursive step
            currList.append(nums[i])
            # one step appending i
            newTotal = total + nums[i]
            dfs(i, currList, newTotal)
            # other step not appending i
            currList.pop()
            dfs(i + 1, currList, total)

        dfs(0, [], 0)
        return res