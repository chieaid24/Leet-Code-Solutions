class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # brute force solution: loop through text1 get a list of all subsequences, then  check if it is a 
        # subsequence of the text2 as well -> O(2^n * m), get the longest one

        # What would the array look like, if for each text1 index, it also stored the text2 starting index
        # this would be an array of n x m
        # If we just had to loop and fill out this array, it would be an O(n * m) solution
        # How do we fill out this array?
        # [3 2 2 1 1] <- starting at text1 index 0
        # [2 2 2 1 1] <- 
        # [1 1 1 1 1] <- starting from text1 index 2 (start from here)
        # if two chars are ==, then ++ the subsequence count, then we can exit / set 
        # entries to the left = to that number (since we can have a max
        # ++ of 1 for each character in text1

        # since you only need to access the row below it, you can probably just store a 1D array and
        # update it each row
        # general algorithm, loop from the last index1, from the last index2. (the row below should be 0s)
        # For each pair of indices, the curr value = (value below + equivalence). Once the first equivalence
        # is found, then for the rest of the entries of the row, just increment immediately and move on
        # This is because the "ideal" match is at the end of the word,, and for every row, we can only find
        # 1 addititional match. IE if not found, curr = (value below + equiv), if found, curr = curr++
        # Then, after looping through all possible pairs, we return dp[0][0] to get the maximum subseq
        # starting at index 0 for both text1 and text2. This has time complexity (O(n * m)) and space (O(n * m))
        # can maybe reduce the space complexity by storing a single row of an array and iterating through it

        # Better way, for our cell, if the characters match, we know that it is 1 + then the max subseq
        # starting from i + 1 and j + 1, so therefore, we do 1 + diag entry
        # If our characters do not match, then we want to take the max between either the i + 1 or the j + 1
        # solutions, as they could be different, but we want to take the max between them, as our subproblem
        # becomes either inc text1 and compare to text2, or inc text2 and compare to text1. (represented by
        # taking the max between our two cells). Then we just loop until the end, which then we return corner
        ROWS, COLS = len(text1), len(text2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                # check equivalence
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        print(dp)
        return dp[0][0]
        # [3 1 1 1 1 0]
        # [2 2 2 1 1 0]
        # [1 1 1 1 1 0]
        # [0 0 0 0 0 0]
        