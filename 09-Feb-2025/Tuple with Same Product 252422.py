# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_count = defaultdict(int)    
        for i in range(1, len(nums)):
            for j in range(i):
                p = nums[i] * nums[j]
                prod_count[p] += 1  
        pairs = 0
        for count in prod_count.values():
            if count > 1:
                pair_count = (count * (count - 1)) // 2
                pairs += pair_count * 8   
        return pairs
