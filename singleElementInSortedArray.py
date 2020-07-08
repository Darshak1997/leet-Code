class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if (mid % 2 == 1 and nums[mid] == nums[mid-1]) or (mid % 2 == 0 and nums[mid] == nums[mid+1]):
                left = mid + 1
            else:
                right = mid
        print(left)
        return nums[left]
            
        
        
        # res = collections.Counter(nums)
        # for i, v in res.items():
        #     if v == 1:
        #         return i
