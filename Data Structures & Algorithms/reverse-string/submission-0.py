class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers, one at each end, and swap the characters
        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        