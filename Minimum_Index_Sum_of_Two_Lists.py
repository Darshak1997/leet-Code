# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        dict2 = {}
        for i1, v1 in enumerate(list1):
            dict1[v1] = i1
            
        for i2, v2 in enumerate(list2):
            dict2[v2] = i2
            
        res = []
        min_index = 10000
        for k in dict1:
            if k in dict2:
                if dict1[k] + dict2[k] < min_index:
                    min_index = dict1[k] + dict2[k]
                    res = [k]
                elif dict1[k] + dict2[k] == min_index:
                    res.append(k)
                
        print(res)
        
        print(dict1)
        print(dict2)
        return res
