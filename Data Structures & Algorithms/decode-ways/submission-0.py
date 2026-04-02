class Solution:
    def numDecodings(self, s: str) -> int:
        # put a "base case" value such that when any of our trees hit the base case of going to the end
        # of the string w/o failing -> return True, ie 1 grouping
        dp = { len(s): 1 } #map from (index: # of groupings possible starting from this index to the end)

        def dfs(i: int) -> int:
            # check our base cases
            # if we've calculated this value already (by default we know end of string == 1 valid mapping)
            if i in dp:
                return dp[i]
            # if this index starts with a 0, then we know it CANT be valid
            if s[i] == "0":
                return 0
            
            # recursive cases
            # first, treat this as a single digit, and pass the rest of the string to the next
            res = dfs(i + 1) 

            # now, treat this as a double digit (making sure it is valid first, if so, then add it to 
            # the # of mappings from this point)
            # double digits must be 1 OR 2, if 1 then second # can be anything, if 2, second # must be < 7
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and int(s[i + 1]) < 7)):
                res += dfs(i + 2)
            # save it to our dp first! So we don't have to recalculate if we get to this i value
            dp[i] = res
            # return number of valid mappings from this point (treat it as 1 + treat it as 2) 
            return res
        
        return dfs(0)
        
        
        
        # brute force: for every index, take a length 1 string, and decode it (check if valid)
        # 
        # implement a recursive problem such that for each index, you take 1 digit or 2 digits, check if 
        # they are valid, then call the function again on the rest of the digits
        # base case is index is at the end, or invalid, in which case it returns 0
        # 
        # Function psuedo:
        # pass in the entire string
        # take JUST the first character and pass the rest to the next call
        # take the first AND the second and pass the rest to the next call
        # if at any point the "current digit" is not valid -> return 0 immediately
        # else, at our base case (at the end of the string) return 1 for a "valid path"
        # O(N^2 ?) time complexity, space complexity of O(1)
        # small optimization, if at any point chunk starts with 0 -> must be invalid so return
        # 
        # we are on the right track with our solution
        # however, we can track the past already calculated values in an array (called dp)\
        # to avoid having to calculate it again when going down that different path
        # since when going down it once, we always know like at the last index, it will ALWAYS be 1 way
        # then like second to last index there's always 2 ways, so then when going down it again,
        # if we had started from the beginning, instead of calculating all the smaller cases again,
        # we can just check our dp cache, to see how many mappings there were in that substring
        # as we calcd it before.

        # this makes sense because when we break it down into subproblems, with our decision tree,
        # we know that once we get to the base case (end) and start propogating up with our total # of
        # values, this will be the same for all routes going back down again (it is a static # of mappings
        # from say, the 3rd to last character)
        # So, once we calculate it once, (by going down the string) we can save it in a dict (from index to
        # value) so that when going down again, this time with a slightly different iteration (but same
        # subproblems, then we can just use what we already calcd)
        # This comes down to identical subproblems that are reached from different beginnings
        # when we see this, we realize that we only have to make these calculations once,
        # store them in an array or a dict, and then when we hit an identical subproblem that we've calcd
        # we can just grab that value instead of recalculating -> connect this to stair problem or fibonacci
        # (1 2 1 2)




