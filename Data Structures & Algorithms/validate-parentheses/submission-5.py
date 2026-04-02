class Solution:
    def isValid(self, s: str) -> bool:
        # data structure -> pairs means use a hashmap
        # data strucutre -> analyze one by one, only matters what the last one is
        # means stack

        closed_to_open = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in closed_to_open.values():
                stack.append(char)
            elif stack and stack[-1] == closed_to_open[char]:
                stack.pop()
            else:
                return False
        # make sure that stack is empty

        return True if not stack else False