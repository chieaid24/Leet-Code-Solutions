class Solution:
    def trap(self, height: List[int]) -> int:
        # at each index, the amount of water stored at that place is the min(maxLeft, maxRight) where maxLeft is the height of any
        # column to the left of the index (serves as the left boundary) and vice versa for maxRight. This min() value serves as the upper bound
        # for the amount of water that can possibly be stored at that index. However, the actual value also depends on the height[index],
        # so the actual amount of water that can be stored is min(maxLeft, maxRight) - height[index]. Conceptually, this is the two highest
        # boundaries that the water must sit between, and the height of the index itself can reduce the amount of water that can be stored
        
        # Implementation: use two pointers to traverse from the ends of the array
        # keep track of the maxLeft and maxRight of both sides as the pointers come together
        # The lesser between maxLeft and maxRight will serve as the "boundary", and will be used to calculate the amount of water at the index
        # For example, if maxLeft is < maxRight, even though we don't know what maxRight actually is, we know that maxLeft MUST be less than
        # maxRight, so we choose maxLeft as our boundary, and imcrement the left pointer. We then recalculate maxLeft, and calculute the amount
        # of water that can be stored at the l index. 
        # Loop until the pointers cross or touch, as they must act as boundaries for the index

         # check base cases
         # n/a

         # initialize variables
         l, r = 0, len(height) - 1
         maxLeft, maxRight = height[l], height[r]
         res = 0

         while l < r:
            # check if maxLeft or maxRight is lesser, incremenet the lesser pointer
            if maxLeft < maxRight:
                # inc left
                l += 1
                # update the max
                maxLeft = max(maxLeft, height[l])
                # update the water amount
                res += maxLeft - height[l]
            else:
                # dec right
                r -= 1
                # update maxRight
                maxRight = max(maxRight, height[r])
                # update the water amount
                res += maxRight - height[r]
         return res