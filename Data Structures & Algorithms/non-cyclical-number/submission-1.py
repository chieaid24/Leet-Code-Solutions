class Solution:
    def isHappy(self, n: int) -> bool:
        # loop using % 10 to break down into digits, and square them
        # use a set to track the numbers that have been seen
        # if it ever equals one, return true
        # once it gets repeated in set() return false

        seen = set()
        while n not in seen:
            seen.add(n)
            # calculate new n
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
        
    def sumOfSquares(self, n) -> int:
        sum = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            sum += digit
            n //= 10
        return sum
