# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        if image[sr][sc] == color:
            return image
        q = deque()
        start_color = image[sr][sc]
        seen = set()
        q.append((sr, sc))
        seen.add((sr, sc))
        image[sr][sc] = color
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def inBounds(r, c):
            return 0 <= r < row and 0 <= c < col
        while q:
            cur_r, cur_c = q.popleft()
            for dr, dc in directions:
                new_r = cur_r + dr
                new_c = cur_c + dc
                if inBounds(new_r, new_c) and image[new_r][new_c] == start_color and (new_r, new_c) not in seen:
                    image[new_r][new_c] = color
                    seen.add((new_r, new_c))
                    q.append((new_r, new_c))
        return image