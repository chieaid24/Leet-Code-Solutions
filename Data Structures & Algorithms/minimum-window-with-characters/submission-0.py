class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use sliding window.
        # have two dicts, one for the (char: occurences) in the window, and another for the
        # occurences in t.
        # This allows you check one by one if a condition is satisfied in the window.
        # Keep a count called "have" and "need" which is the number of letter conditions satisfied
        # this allows you to easily see whether the entire window is valid or not, without looping through
        # all of the conditions again (O(1) instead of O(n))
        
        # algorithm. Loop through using sliding window, adding the char to the window dict
        # Once the conditions have been met (have == need), record the res indices, and then pop left
        # Both popping from the window dict, updating have, and incrementing the L pointer
        # This should be a while loop such that have == need, since once this is not a thing
        # we keep sliding the right again until the end to find new characters.
        # when the r pointer reaches the end, return the length (if exists) if not, then return empty
        # string
        
        # Let's first create the dict containing the chars in t
        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        # init our variables
        l = 0
        have, need = 0, len(countT)
        res, resLength = [-1, -1], float("infinity")
        
        for r in range(len(s)):
            # get the char
            char = s[r]
            # add it to the window count
            window[char] = 1 + window.get(char, 0)
            # now check if you have to increment the "have" flag
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # while loop to pop from left until have != need
            while have == need:
                # record the res
                if r - l + 1 < resLength:
                    res = [l, r]
                    resLength = r - l + 1
                # pop left
                window[s[l]] -= 1
                # decrement have if needed
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l +=1
        l, r = res
        return s[l:r + 1] if resLength != float("infinity") else ""


