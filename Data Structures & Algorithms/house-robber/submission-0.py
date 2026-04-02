class Solution:
    def rob(self, nums: List[int]) -> int:
        # we want to look at this from a DP perspective
        # for every num in nums, we can either 1) skip it, or 2) include it
        # if 1) then we want to add the previous maximum amt + the amount after it
        # if 2) we want to add the one BEFORE the previous sum + this number

        # the subproblem is that once you skip it, you have to calculate the maximum robbed of the 
        # rest of the array, and add it n - 1
        # if you include it, then you can't include the last one, but you want to add it to the max
        # create before (already completed subproblem)
        # therefore, we can use a memoization strategy, where we can track the maximum amt at each index
        # such that we can access this, and then update that as we roll along each num
        # as you can see by our two cases, we only need to access n - 1 (if we skip) or n - 2 (if we include)
        # therefore, we can just store the last two numbers, and update as we go, instead of storing
        # the entire array

        # this is kind of like reducing to subproblems, and then keeping track of our "runnning total"
        # at each index what is the maximum amt we can steal up until this point
        # then, when solving for each value, we can consider our decision tree to see "if this was the last
        # value, how would I calculate maximum amt?"

        # create a running maximum at each index, if we were to include that index in our total
        twoAway, oneAway = 0, 0
        for n in nums:
            # two cases, and we want to find the max between them
            # first case: we include this n, that means we want this n + the twoAway (the max we can
            # get if we skipped the last one)
            # second case: we skip this n, that means that the max is just going to equal the oneAway,
            # since that would represent the maximum amt that could be reached at that point
            # this would then, make the index at this value in our memo array, the maxmimum amt of money
            # we could rob at this point. We then carry this on to the next n's, to reach the end of the 
            # array
            curr = max(n + twoAway, oneAway)
            twoAway = oneAway
            oneAway = curr
        return oneAway
