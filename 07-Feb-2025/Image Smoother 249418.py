# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = []
        
        rows = len(img)
        cols = len(img[0])
        ans = [[0]*cols for _ in range(rows)]
        for i in range(rows): # 0 1 2
            for j in range(cols): # 0 1 2
                directions.append((i,j))
        
        def inbound(x,y):
            return ((0 <= x < rows) and (0 <= y < cols))

        for i,j in directions:
            sum =0
            count = 0
            for x in (i-1,i,i+1):
                for y in (j-1,j,j+1):
                    if inbound(x,y):
                        sum += img[x][y]
                        count += 1
            ans[i][j] = sum//count
        return ans