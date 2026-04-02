class KthLargest:
    """
        We want to store the k largest values in some data structure, have them be sorted
        and then return the minimum of those values as the return value for add()
        This sounds like a minHeap of size k.
        When we initialize, create a minHeap with nums (Ologn), and then pop (Ologn) until there are k 
        values in the heap.
        When adding, if the heap is full, then check if the added val is greater or equal to the 
        heap[0] (minimum value) which
        means that we should add it to the heap, and then pop() again if there are too many values.
        If heap isn't full, just add it, and then return the minimum value in the heap or heap[0] 
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # pop values if needed
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val >= self.minHeap[0]:
            # add and pop
            heapq.heappush(self.minHeap, val)
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
