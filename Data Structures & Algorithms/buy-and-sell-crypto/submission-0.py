class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # have two pointers, one for the right and one for the left. 
        # the right will increment until the end. if left greater than right,
        # slide the window right. if right greater than left, move the right
        # further down and compare, once its lower, then move the left and right
        # together so can keep checking after that for maxes
        left_ptr, right_ptr = 0, 1
        max_profit = 0

        while right_ptr < len(prices):
            if prices[right_ptr] > prices[left_ptr]:
                curr_diff = prices[right_ptr] - prices[left_ptr]
                max_profit = max(max_profit, curr_diff)
                
            else:
                left_ptr = right_ptr
            right_ptr += 1
        return max_profit
        