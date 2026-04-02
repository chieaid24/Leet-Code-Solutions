class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first could run a O(n^2) where loop through each and compare to each

        # second could have 2 pointers, slide until right > left. extend right
        # until right <= left, then move left and right to that value
        # and continue from there

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                curr_profit = prices[right] - prices[left]
                max_profit = max(curr_profit, max_profit)
                right += 1
            else:
                left = right
                right += 1
        return(max_profit)