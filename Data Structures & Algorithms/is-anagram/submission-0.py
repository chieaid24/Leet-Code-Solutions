class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both strings
        s_list = list(s)
        t_list = list(t)
        # check if equal
        s_list.sort()
        t_list.sort()
        if (s_list == t_list):
            return True
        return False