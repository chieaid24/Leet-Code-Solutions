class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search in rotated array
        # use normal binary serach
        # How can we figure out whether to search the left or the right half of the array?
        # If we know the middle is in the left sorted partition
        #   Then depending on our target in relation to the left pointer, we know 
        #   whether to search the left or the right portion (if the target is less than the left poitner
        #   then we know that it must lie on the right)
        #   Else, check the left
        # If we know the middle is in the right sorted partition
        #   again, depending on our target in relation to the right pointer
        #   IF the target is greater than the right pointer -> it must be on the left
        #   If not, it must be on the right

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # figure out if m is in the left partition or right partition
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target < nums[l]:
                    # search the right
                    l = m + 1
                elif target > nums[m]:
                    # search the right
                    l = m + 1
                else:
                    # seach the left
                    r = m - 1 
            # right partition
            else:
                if target > nums[r]:
                    # search the left
                    r = m - 1
                elif target < nums[m]:
                    # search the left
                    r = m - 1
                else:
                    # search the right
                    l = m + 1
        return -1
