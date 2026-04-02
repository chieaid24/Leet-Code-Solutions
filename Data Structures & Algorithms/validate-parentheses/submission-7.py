class Solution:
    def isValid(self, s: str) -> bool:
        # create a dict from ] -> [
        # loop through each letter of the string, adding to a stack if
        # in the dict.value
        # if it a dict.key, find the corresponding open bracket in the 
        # last added Q value, and pop it
        mappings = {")": "(", "]":"[", "}":"{"}
        stack = []
        # loop through the letters
        for char in s:
            if char in mappings.values():
                stack.append(char)
            else:
                if stack and mappings[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
