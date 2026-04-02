class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # go through the first one initially
        # for each string, go through it until it doesn't match, then cut the res string
        # keep comparing to the res string until all of the strings have been checked or res is null
        res = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(res) and i < len(s) and res[i] == s[i]:
                i += 1
            res = res[:i]
        return res