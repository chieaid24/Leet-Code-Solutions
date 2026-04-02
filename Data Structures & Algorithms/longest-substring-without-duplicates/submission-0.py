class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: loop through each character and check all possible substrings starting at that character
        # sliding window:
        # Two pointers and a set, if within our "window" we have repeating characters, increment the left pointer until
        # the repeating character is gone, and continue
        # have a variable that tracks the max length of the set for each step
        # the maxiumum length is the max length of the set

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                # pop values from the left until this is not true
                charSet.remove(s[l])
                l += 1
            # add the new character to the set
            charSet.add(s[r])
            # find the current max length
            # could use len(charSet) -> O(n), but easier to just do (r - l) + 1
            res = max(res, r - l + 1)
        return res

