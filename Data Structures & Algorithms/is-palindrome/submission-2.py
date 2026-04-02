class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first format the string such that it can be parsed
        # the key is isalnum() which returns true if alphanumerical
        # then have two pointers, increment through the string, if ever
        # not equal then return false
        
        # init pointers
        left = 0
        right = len(s) - 1
        
        while (left <= right):
            # check if value is numerical
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
