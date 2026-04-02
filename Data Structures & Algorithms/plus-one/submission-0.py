class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # loop through the list right to left
        # on the first digit, add one, and if the value is != 10, then break and return
        # if it is = 10, then increment a carry bit, and modulo 10, 8 ,6 9
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits