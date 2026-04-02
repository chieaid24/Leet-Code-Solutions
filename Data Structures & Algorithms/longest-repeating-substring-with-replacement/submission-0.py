class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute force: For each letter, replace the next k non matching letters, and find that longest substring
        # repeat for every character in the string

        # Sliding window technique: we can see that using the k value, that for every substring, it is "valid" if it has a maximum
        # of k "differences" to the "target letter". So use sliding window to loop through the string, and once this is not valid,
        # then pop from the left until it is valid

        # you can do this by having a array / dictionary of all the letters and their occurences in the window. Then find the most common letter,
        # and base the isValid condition off of that (other letters besides most common <= k)

        # intuition here: substring -> sliding window. we know that k letters in a substring can be "wrong" and the substring is still valid
        # so we need some way to check each letter that is in our window. We want to use the highest occuring letter as our base letter
        # and compare other letters with k.
        # For each iteration, update a res for the maximum substring length

        # init variables
        l, r = 0, 0
        letterDict = defaultdict(int) # letter: occurences
        maxLength = 0

        # main loop
        while r < len(s):
            # add the new letter to letterDict
            letterDict[s[r]] += 1

            # check the validity of the list

            # get "target" letter -> the letter with most occurences in the dict
            # do a while loop incremeneting the left pointer while the list is invalid
            # list is invalid when the length of the window - max of the letterDict is greater than k
            while (r - l + 1) - max(letterDict.values()) > k:
                # increment l, and also update the letterDict
                letterDict[s[l]] -= 1
                l += 1
            
            # now that the list is valid, update the maxLength, and incremenet r
            maxLength = max(maxLength, (r - l + 1))
            r += 1
        return maxLength