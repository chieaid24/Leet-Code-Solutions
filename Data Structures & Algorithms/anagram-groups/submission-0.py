class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force is creating an array of sets corresponding to each anagram
        # if the word fits that set, label it so and push to a final list
        # o(n^2) time, o(n) space
        
        # make it easier by not using sets, instead sorting each word alphabetically, 
        # adding them to the outputs (sorted_word: [list]) -> return keys
        
        # sorted strategy
        pairs = {}

        for string in strs:
            alphaStr = ''.join(sorted(string))
            if alphaStr in pairs.keys():
                pairs[alphaStr].append(string)
            else:
                # add it to the pairs
                pairs[alphaStr] = [string]
        return list(pairs.values())
