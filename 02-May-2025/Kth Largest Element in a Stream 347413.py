# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:
    def __init__(self, k: int, nums: List[int]):   
        self.k=k
        self.h=nums
        heapq.heapify(self.h)
        while len(self.h)>self.k:
            heapq.heappop(self.h)
    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if len(self.h)>self.k:
            heapq.heappop(self.h)
        return self.h[0]