class Solution:
    def reverseBits(self, n: int) -> int:
        # brute force, convert from bin -> string, replace, convert back to int

        #bit mask -> loop through right to left, and copy the value to the left of a new bin number
        res = 0

        for k in range(32):
            digit = n >> k & 1
            res += digit << (31 - k)
        return res