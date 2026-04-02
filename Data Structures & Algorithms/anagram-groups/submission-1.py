class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first pass: sort every entry, create a dict of that entry -> list of anagrams
        # return the keys
        # time O(n * nlog(n)) space O(n)

        # create dict of {sorted -> [anagrams]}
        unique = {}

        # loop through the strs, sort them, add them to unique
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in unique:
                # append it to the list
                unique[sortedString].append(s)
            else:
                unique[sortedString] = [s]
            print(unique)
        
        # return the values
        res = []
        for key, value in unique.items():
            res.append(value)
        return res