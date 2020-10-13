class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        changeColor = image[sr][sc]
        if changeColor == newColor:
            return image
        self.dfs(image, sr, sc, newColor, changeColor)
        return image
        
    def dfs(self, image, i, j, newColor, changeColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != changeColor:
            return
        image[i][j] = newColor
        self.dfs(image, i+1, j, newColor, changeColor)
        self.dfs(image, i-1, j, newColor, changeColor)
        self.dfs(image, i, j+1, newColor, changeColor)
        self.dfs(image, i, j-1, newColor, changeColor)
