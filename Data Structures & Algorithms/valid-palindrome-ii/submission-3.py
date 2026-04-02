class Solution:
    def validPalindrome(self, s: str) -> bool:
        # use two pointers, if at any point it's not equal to, either increment one or the other
        # since it MUST be equal -> if not return False
        # also, if another hiccup happens then return False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # check if the substring without l or without r is valid
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True
        
        
        
        #rbacecar