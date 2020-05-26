class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        Flag = False
        for i in range(len(matrix)):
            Flag = self.bs(matrix[i], 0, len(matrix[i])-1, target)
            if Flag == True:
                return True
            else:
                continue
        return False
            
    def bs(self, arr, l, r, x):
        while l<=r:
            mid = l + (r - l) // 2; 
            if arr[mid] == x: 
                return True
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
