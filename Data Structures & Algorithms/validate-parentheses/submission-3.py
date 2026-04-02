class Solution:
    def isValid(self, s: str) -> bool:
        def peek(my_list):
            return my_list[-1]
        
        map_key = {")": "(", "]": "[", "}": "{"}
        my_stack = []    
        for char in s:
            try:
                if char in map_key.values():
                    my_stack.append(char)
                elif map_key[char] == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            except Exception as e:
                return False
        
        return len(my_stack) == 0
            