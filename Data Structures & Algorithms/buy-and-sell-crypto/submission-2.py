class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop through the list once
        # track left and right indexes, the right is the one that is incremented
        # if right is less that left, make left equal right 
        #   since we want to always buy the smallest value
        # keep track of max output
        # keep sliding right pointer as it increases until the end, 
        # finding the max between old max and new potential value
        l, r, profit = 0, 0, 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            currProfit = prices[r] - prices[l]
            profit = max(profit, currProfit)
            r += 1
            print(l, r, profit)
        return profit
            

