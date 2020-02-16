# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, j  in enumerate(nums):
            val = target - j
            if val not in hashmap:
                hashmap[j] = i
            else:
                return [hashmap[val], i]
        
        # Brute Force Method #
        # res = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             if nums[i] + nums[j] == target:
        #                 if i not in res: res.append(i)
        #                 if j not in res: res.append(j)
        #             else:
        #                 continue
        # return res
