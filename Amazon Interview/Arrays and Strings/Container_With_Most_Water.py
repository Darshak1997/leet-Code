class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        start = 0
        end = len(height) - 1
        
        for i in range(len(height)):
            
            width = abs(start - end)
            
            if height[start] < height[end]:
                res = width * height[start]
                start += 1
            else:
                res = width * height[end]
                end -= 1
            
            water = max(res, water)
            
        return water
        
        
#         start = 0
#         end = len(height) - 1
#         maxArea = 0
        
#         while start < end:
#             currArea = min(height[start], height[end])*(end - start)
#             maxArea = max(maxArea, currArea)
#             if height[start] <= height[end]:
#                 start += 1
#             elif height[start] > height[end]:
#                 end -= 1
            
#         return maxArea
