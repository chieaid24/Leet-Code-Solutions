class Solution:
    def findMin(self, nums: List[int]) -> int:
        # intuition: use binary search since it sorted, and also need to use log(n) time
        # trying to find where the lower values are (search there next to find the minimum value)
        # and at any m point that we choose, update a minValue flag. 
        # If the left is increasing correctly, and the right is not, then look on the right
        # because that's where the pivot is
        # if the left and right are increasing correctly, look on the left because it's sorted correctly,
        # so the lower values will be towards the left
        
        # if the range between r and l is ever sorted, just take the left-most and update that
        # because the middle value could be the minimum (and with binary search it's impossible to get
        # to that value, we have to consider it as a minimum by using min() function) 
        # 4, 1, 2, 3

        # apply binary search. If the entire window is ever sorted, use the left pointer as the final
        # value we will check (base case).
        # if the nums[l] <= nums[m], the we should check right since when we rotate the array, the lower
        # values go to the right (if it rotates all the way around it is sorted again)
        # if this isn't true, then we check the left since we know that the pivot spot is somewhere on
        # the left
        # 4, 1, 2, 3 

        # base case
        if len(nums) == 1:
            return nums[0]
        
        # init variables
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # base case if the window is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # find m
            m = (l + r) // 2
            res = min(res, nums[m])

            # decide which portion to search
            if nums[l] <= nums[m]:
                # search right
                l = m + 1

            else:
                # search left
                r = m - 1
        return res
