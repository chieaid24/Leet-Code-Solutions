class MedianFinder:
    # Lets use 2 heaps, a maxHeap to store the smaller values (we will initially add vall values to this heap
    # and then compare if we need to change things around to make them valid + balanced)
    # and a minHeap to store the larger values
    # then, calculating the median is trivial, and adding / removing elements is O(logn) rather than O(n)
    def __init__(self):
        self.smallHeap, self.largeHeap = [], []

    def addNum(self, num: int) -> None:
        # add it to the smallHeap (it's a maxHeap)
        heapq.heappush(self.smallHeap, -num)

        # we need to make sure that 1) the max value of smallHeap is < min value of bigHeap
        # 2) sizes are close to equal
        while self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
        # check sizes
        while len(self.smallHeap) > len(self.largeHeap) + 1:
            # move from smallHeap to largeHeap
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
        while len(self.largeHeap) > len(self.smallHeap) + 1:
            heapq.heappush(self.smallHeap, -heapq.heappop(self.largeHeap))
    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -float(self.smallHeap[0]) if self.smallHeap[0] else 0.0
        elif len(self.smallHeap) < len(self.largeHeap):
            return float(self.largeHeap[0])
        else:
            # find median
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2
        