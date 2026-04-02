class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force: check every single substring, and then check if it is a palindrome with 2 pointers
        # this is a O(N^3) time complexity -> O(n^2) for every substring, and O(n) to check if its a pal
        # since duplicate strings are allowed -> leads me to believe that a possible solution is linearly
        # checking every character as if it is the center of an odd pal and center of an even pal
        # we just inc the count for every loop that executes
        # This solution is O(2*N^2), where we check every char and then we check other char that could
        # be a pal. Space O(1) since just need constant space (integers)

        res = 0
        for i in range(len(s)):
            # check if it is the center of an odd palindrome
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # check if it is the center of an even palindrome
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res