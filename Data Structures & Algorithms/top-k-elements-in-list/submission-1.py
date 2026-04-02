class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through once to get a dict of the count of each value
        # can use a bucket sort to sort the values based on their count in an array, since there
        # is a maximum of len(nums) unique values and a minimum of 1 unique value

        # first create the dict keeping count of each number
        numCount = defaultdict(int) # something -> int, default 0
        for num in nums:
            numCount[num] += 1
        print(numCount)
        # now create a bucket (an array of lists) that will hold the count of each number
        bucket = [[] for k in range(len(nums) + 1)]
        print(bucket)
        for num, count in numCount.items():
            bucket[count].append(num)

        res = []
        # now loop through this bucket to find the k # of highest values
        for index in range(len(bucket) - 1, 0, -1):
            for val in bucket[index]:
                res.append(val)
                if len(res) >= k:
                    return res
                print(res)


            
