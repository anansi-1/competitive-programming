# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cur_count = 0
        max_fruit = float("-inf")
        l =0 
        fruit_count = {}
        for r in range(len(fruits)):
            fruit_count[fruits[r]] = fruit_count.get(fruits[r],0)+1
            cur_count += 1
            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                cur_count -= 1
                l += 1
            max_fruit = max(cur_count,max_fruit)
        
        return max_fruit

