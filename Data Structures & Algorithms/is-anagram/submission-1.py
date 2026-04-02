class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first pass is to loop through both, adding each to a dictionary
        # with {letter, instances} and then equate the two

        #second pass, convert each to a list, sort the list, then compare
        #use the sorted() function, which takes an iterable like a string
        # returns a list of sorted
        return sorted(s) == sorted(t)