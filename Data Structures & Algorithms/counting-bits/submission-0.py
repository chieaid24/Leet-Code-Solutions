class Solution:
    def countBits(self, n: int) -> List[int]:
        # loop up until n
        # convert each to binary, and count 1s

        res = []
        for k in range(n + 1):
            res.append(bin(k).count('1'))
        return res