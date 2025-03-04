# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bill = 0
        ten_bill = 0
        for i in bills:
            if i ==5:
                five_bill += 1
            elif i == 10:
                ten_bill += 1
                if five_bill:
                    five_bill -=1
                else:
                    return False
            elif i == 20:
                if five_bill and ten_bill:
                    five_bill -=1
                    ten_bill -= 1
                elif five_bill >= 3:
                    five_bill -= 3
                else:
                    return False
        return True