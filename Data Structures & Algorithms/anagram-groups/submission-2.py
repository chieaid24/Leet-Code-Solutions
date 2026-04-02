class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first pass: sort every entry, create a dict of that entry -> list of anagrams
        # return the keys
        # time O(n * nlog(n)) space O(n)

        # create dict of {sorted -> [anagrams]}
        # unique = {}

        # can create a default value for my dict by doing a defaultdict
        unique = defaultdict(list)

        # loop through the strs, sort them, add them to unique
        for s in strs:
            sortedString = "".join(sorted(s))
            # since we now how a default list ([]) created for non existing keys
            # if sortedString in unique:
            #     # append it to the list
            #     unique[sortedString].append(s)
            # else:
            #     unique[sortedString] = [s]
            unique[sortedString].append(s)
        
        # return the values
        # since unique.values() returns a view object, must convert it to a list (easy)
        return list(unique.values())