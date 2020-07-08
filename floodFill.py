class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.initial = image[sr][sc]
        self.dfs(image, sr, sc, newColor)
        return image
    
    def dfs(self, image, i, j, newColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j] != self.initial:
            return
        image[i][j] = newColor
        self.dfs(image, i+1, j, newColor)
        self.dfs(image, i-1, j, newColor)
        self.dfs(image, i, j+1, newColor)
        self.dfs(image, i, j-1, newColor)
        
