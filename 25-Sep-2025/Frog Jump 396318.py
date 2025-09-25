# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool: 
        if stones[1] != 1:
            return False    
        queue = [(1,1)]
        seen = set()

        while queue:
            stone_num, k = queue.pop(0)
            if stone_num == stones[-1]:
                return True
            
            for neib in [k-1,k,k+1]:
                next_pos = stone_num + neib
                if next_pos == stone_num:
                    continue
                
                if next_pos in stones and (next_pos,neib) not in seen:
                    queue.append((next_pos,neib))
                    seen.add((next_pos,neib))
        return False

    def helper(self,stones, stone_num,k):
        stone_num += k
        if stone_num == stones[-1]:
            return True
        if stone_num > stones[-1]:
            return False
        if stone_num not in stones:
            return False
        
        less = False
        if k >1:
            less = self.helper(stones,stone_num,k-1)
        same = self.helper(stones,stone_num,k)
        more = self.helper(stones,stone_num,k+1)

        return less or same or more