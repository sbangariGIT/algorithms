class Solution:
    def helper(self, image, sr: int, sc: int, color: int, start: int, visited: set):
        if sr < 0 or sc < 0 or sr > len(image) - 1 or sc > len(image[0]) - 1:
            return
        if image[sr][sc] != start:
            return
        image[sr][sc] = color
        visited.add((sr, sc))
        if (sr + 1, sc) not in visited:
            self.helper(image, sr + 1, sc, color, start, visited)
        if (sr - 1, sc) not in visited:
            self.helper(image, sr - 1, sc, color, start, visited)
        if (sr, sc + 1) not in visited:
            self.helper(image, sr, sc + 1, color, start, visited)
        if (sr, sc - 1) not in visited:
            self.helper(image, sr, sc - 1, color, start, visited)

    def floodFill(self, image, sr: int, sc: int, color: int):
        if sr < 0 or sc < 0 or sr > len(image) - 1 or sc > len(image[0]) - 1:
            return image
        self.helper(image, sr, sc, color, image[sr][sc], set())
        return image
        