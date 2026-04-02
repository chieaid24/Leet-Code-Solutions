class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force: start at 0, add 1 or 2 as long as less than the top

        one = 1
        two = 1

        for k in range(n - 1):
            temp = one
            one = one + two
            two = temp 
        return one