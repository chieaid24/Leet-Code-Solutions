class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force: check every substring -> check if palindrome, running var of max substring.
        #  o(n^3) time (all substrings * time it takes to check if palin), o(1) space

        # look for a better solution:
        # instead of checking each substring, we can just check every index, and see the longest
        # palindrome it can create if it was the center. Do this by stepping out to both sides
        # however, if the palindrome is even (example 2 case) for each edge, we need to check if
        # it is == to our current letter, if so, then add +1 to the length of palindrome, and `continue`
        # now, we check each character O(n) and for each character, we maximum check all of the other characters
        # this gives a time complexity of O(n^2)
        maxLen, res = 0, ""

        for i in range(len(s)):
            # we can solve this by just treating each index as either: a center of an odd palindrome
            # in which we just expand outward

            # or we can treat it as an even palindrome where we start our two pointers next to each other
            # this gives us two discrete cases, since it is difficult to combine them into one 
            # always consider this to be a possibilty when trying to solve these, as a longer time 
            # complexity is okay, if it works!

            # first, let's consider the index as a center of an odd
            l, r = i, i
            # both loop and conditional!
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # ie it is always valid when it hits this loop (only covers odd cases)
                # check if its a max
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # now lets act as if this index is the center of an even palindrome 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
                        

                
