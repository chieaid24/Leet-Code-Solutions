class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack and a map, because each ( has its ). 
        # loop through the string, for each char, if the char is an open one
        # check using the maps. and add it to the stack.
        # elif the peek() value and the char correspond to each other,
        # pop the stack. all else return False
        stack = []
        open_to_close = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in open_to_close:
                stack.append(char)
            elif stack and open_to_close[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return True if not stack else False