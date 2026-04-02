class Solution:
    def isPalindrome(self, s: str) -> bool:
        # one variable keeps track of end 
        # in while loop intializes another pointer keeps track of beginning
        # when beg pointer is greater than or equal to end ptr, exits
        # checks if beg and end ptr's string is alphanumeric, if not, increment
        # equates the two values, if they are not equal at any time, return False
        end = len(s) - 1
        beg = 0
        while beg <= end:
            if not s[beg].isalnum():
                beg += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[beg].lower() != s[end].lower():
                return False
            beg += 1
            end -= 1
        return True