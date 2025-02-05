# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pair = defaultdict(list)
        minimum = float('inf')
        for i in range(len(list1)): # 0 1 2
            if list1[i] in list2:
                index_sum = i + list2.index(list1[i]) 
                pair[index_sum].append(list1[i])
        for i in pair:
            minimum = min(i,minimum)

        return pair[minimum]