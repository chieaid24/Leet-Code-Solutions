class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # brute force solution: 
        # starting from the left coin, find the minimum # of coins with JUST that coin, where we can
        # reach that amount 
        # With this type of DP we'd make an array that is length `amount`. Then for each value (0, 1, 2...)
        # and for our first row (coins[0]), we'd find the minimum # of coins we can use with JUST that coin
        # for each column. Then, we move onto the second row, where we consider the 5 coin too, taking the min
        # num of coins now with the ability to use 5 as well. Any leftover space (sub problem) can be 
        # gotten from our previous entry! Where we know that it is the minimum leftover space so far!
        # additionally, we can use any multiple of the coin to achieve it, and if the coins are sorted 
        # this will work. Then, our final # of coins is in the last spot in the 2D dp array.
        # Time O(n * m) where n is the # of coins, and m is the amount

        # greedy solution: which means that we always take with the largest coin we can, then go down the
        # values of the coins until we reach 0. 
        # However, if we cannot reach 0 by taking the maximum amt of large coins, we must backtrack and
        # go down the path with a different # of large coins (ex [2 3] amt=7).
        # Not sure how we can solve it this way, althoguh it does seem better with less iterations
        # NOT GOING TO WOKR!

        # We will arrive at a similar opatimzation of the first brute force, where we can 
        # do bottom up processing, where we start at amount = 0, but we loop thru and consider ALL coins
        # and track it in a 1D array. This has the same time complexity, but less space complexity, since
        # we just need to take the min coins between choosing coin 1, coin 2, etc. This means for each
        # amount, we choose to pick each coin, calculate the amt of coins total it would be (using our
        # dp cache) and then the value at that index would be that min # of coins to fill up that amount
        # Time O(n * m) space O(m)

        dp = [0] * (amount + 1)
        for amt in range(1, len(dp)):
            # loop through each coin and subtract it
            currMin = float("inf")
            for coin in coins:
                remaining = amt - coin
                if remaining >= 0 and dp[remaining] != float("inf"):
                    currMin = min(currMin, 1 + dp[remaining])
            dp[amt] = currMin
        print(dp)
        if dp[-1] == float("inf"):
            return -1 
        else:
            return dp[-1]
        # [5 10] 15
