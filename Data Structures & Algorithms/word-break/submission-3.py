class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute force solution:
        # Break down into EVERY substring, check if each substring is in wordDict, if not continue
        #
        # Better solution  (brute force)
        # Scan through s from index 0, when we find a word in our wordDict, then call
        # recursively with the rest of the string
        # Then continue on, calling every word that exists from the start
        # At each step, one of its recursive children must return True for the total function to 
        # return True

        # A couple optimzizations we can see: 
        # By scanning through every prefix (n), this will lead to O(n^2) scans since we start at every 
        # index and scan the rest of the array. However, by our constraints, we see that wordDict.length
        # is less than s.length, so we can also go about this by for every starting position,
        # loop through our wordDict to see which word fits starting at that index! This gives a 
        # O(n*m) loops throughout the s. Multiply by O(n) for comparing the two, results in a O(n^2 * m)
        # solution
        
        # Additionally, we can do a bottom up solution -> since our solutions towards the beginning
        # of the string depend on the subproblems of the end of the string.
        # This means we can loop through the string from the end, and create a dp cache, storing whether
        # or not we can reach the end of the string from that index. (Still O(n*m)). Then, when we look
        # at indices that are towards the beginning, and if a string of length 4 is valid, then we
        # can set that dp entry to dp[curr + len(w)]. Then we can just return the value of dp[0] (whether
        # or not we can reach the end from the 0th index). This still handles multiple routes of going
        # down, because we still check starting from every index, so as we go down alternate paths,
        # we can see if any of those subproblems are true, and return the OR of those.
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # if we get to the exact end of the word, then it is a valid solution 
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                validWord = True
                for j in range(len(word)):
                    if i + j >= len(s) or s[i + j] != word[j]:
                        validWord = False
                        break
                if validWord:
                    dp[i] = dp[i] or dp[i + len(word)]
        return dp[0]

        # ["abcd"] [a abc b cd]
        # i = 2
        # dp = [0 0 0 1] 