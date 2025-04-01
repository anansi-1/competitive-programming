# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.arr = []    
        self.zero_count = [] 
        self.product = 0

    def add(self, num: int) -> None:
        if self.product == 0:   
            self.arr.append(num)
            self.product = num
        else: 
            self.product *= num
            self.arr.append(self.product)  
        if len(self.zero_count) == 0:   
            if num != 0:
                self.zero_count.append(0)
            else:
                self.zero_count.append(1)
        else:       
            if num != 0:
                self.zero_count.append(self.zero_count[-1])
            else:
                self.zero_count.append(self.zero_count[-1] + 1)
    def getProduct(self, k: int) -> int:
        n = len(self.arr)
        if n - k == 0 and self.zero_count[-1] > 0 :
            return 0
        elif n - k == 0:
            return self.arr[n-1]
        if self.zero_count[-1] - self.zero_count[n-k-1] > 0:
            return 0
        elif self.arr[n-k-1] != 0:
            return self.arr[n-1] // self.arr[n-k-1]
        else:
            return self.arr[n-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)