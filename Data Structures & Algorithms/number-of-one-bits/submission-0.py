class Solution:
    def hammingWeight(self, n: int) -> int:
        # brute force -> mod 2 == 0 add one, then int divide by 2 until equal to 0
        # return bin(n).count('1')

        # create bit mask using left shift
        total = 0
        for k in range(32):
            # bit mask
            if 1 << k & n:
                total += 1
        return total