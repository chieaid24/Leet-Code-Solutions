class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we want to use a maxHeap to store all of the stones, so we can pop the largest two in O(1) time
        # and then add them back in in O(logn) time if there are remaining weight. Go until the heap is 
        # length 1. We can do a max heap if we invert the weights of the stones (so the heaviest ones
        # become most negative)

        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            remaining = -abs(stone1 - stone2)
            if remaining:
                heapq.heappush(stones, remaining)
        return -stones[0] if stones else 0