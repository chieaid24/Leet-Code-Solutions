class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # first pass: iterate from right to left,
        # keeping track of the current max (also set the last value
        # to = -1)
        # then loop all the way to index 0
        currMax = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            # update the value first, then update currMax
            temp = arr[i]
            arr[i] = currMax
            currMax = max(currMax, temp)
        return arr

        # max = 5
        # [5 5 3 2 2 -1]