# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            if image[sr][sc] == color:
                return image
    
            orginal = image[sr][sc]
            queue = deque()
            queue.append((sr,sc))

            while queue:
                x,y = queue.popleft()
                image[x][y] = color
                for r,c in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (0 <= r < len(image) and 0 <= c < len(image[0])) and image[r][c] == orginal:
                        queue.append((r,c))
            return image