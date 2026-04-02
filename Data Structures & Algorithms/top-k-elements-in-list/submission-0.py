class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first pass brute force -> create a mapping keeping track of all (num -> instances)
        # sort by the keys (with lambda function), and return the k largest values
        # sorting is nlogn
        
        # ------
        # use bucket sort -> basically counting the # of occurences as the index, and then the value of the array is 
        # the unique number that has that count (should be a list)

        # first thing is to have a hash map that is tracking counts, insert that map into a bucket (array) based on
        # the occurencies (the map's key -> index)
        # loop from the end of the array down to get the K values, appending each cell to the array
        # -------

        # create map
        frequency = {} # num -> occurences

        for num in nums:
            # possibly remove this if statement completely
            if num in frequency:
                # increment
                frequency[num] += 1
            else:
                # add a new one
                frequency[num] = 1


        # create our bucket
        bucket = [[] for _ in range(0, len(nums) + 1)]
        # for each key in frequency, append the key to index value
        for key, value in frequency.items():
            bucket[value].append(key)
        print(bucket)
        # get the k largest indexed keys
        output = []
        for index in range(len(bucket) - 1, 0, -1):
            if len(output) >= k:
                return output
            for num in bucket[index]:
                output.append(num)
            
        return output

            
