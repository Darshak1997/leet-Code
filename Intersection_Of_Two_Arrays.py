# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

class Solution:
    def self_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.self_intersection(set1, set2)
        else:
            return self.self_intersection(set2, set1)
        
        
        
        # BRUTE FORCE METHOD #
        # intersect = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             if nums1[i] not in intersect:
        #                 intersect.append(nums1[i])
        # return intersect
