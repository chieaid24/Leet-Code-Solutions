class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # brute force is find cost if taking one step, and then two steps, find minimum cost
        # recursive

        for i in range(len(cost) - 2, -1, -1):
            one = cost[i + 1]
            two = cost[i + 2] if i + 2 < len(cost) else 0
            cost[i] = min(cost[i] + one, cost[i] + two)
        return min(cost[0], cost[1])