class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Brute force solution:
        # Starting at every index, loop through the rest of the array. If the number is larger than
        # the last, skip it. If it is smaller, split into two decision trees, one where you skip it
        # and one where you make it the new "last". Go until end, keep track of the total length
        # of the subsequence, return the longest one.
        # O(2^n)

        # Current algorithm: work backwards, for each index, check if it is less than the "last" index
        # if it is, then add increment one for the subsequence. If not, then take the last subsequence
        # for this index.
        #
        # need to track curr min
        # if we track our curr minimum in the array, and our new value (which is less than the last value)
        # is less than our curr minimum, then we know we can increment.
        # if it is equal to or greater than, we just keep it the same?
        # To solve this, think of increasing the time compleixty!
        # instead of tracking a single min, let's just check ALL of the past subsequences, and find the 
        # max between them.
        # In this approach, we MAKE SURE that all possibilities are evaluated, and we take the max between
        # them. We have to do this, since by our examples before, just tracking a "minimum" is not enough
        # information to keep track of the increasing subsequences of past. 
        # We can more simply do this, by just checking each one! Ie checking if this num is less than
        # any of the past numbers, and if so, then take max(1 + dp[past_num]... All past numbers)
        # This is because there could be any amount of re-increasing patterns throghout the sequence, ie
        #[1 2 3 2 3 4 1 2 3], where for each new number, we don't know what the last min is, or what
        # sequences we are currently tracking (especally when it gets large). ie there could be an infinite
        # number of "starts" as our array gets longer. This means that an easy approach is to just loop
        # through every one, and take the max, which would be O(n^2), a big increase from o(n).
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            # check it against all past numbers
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)