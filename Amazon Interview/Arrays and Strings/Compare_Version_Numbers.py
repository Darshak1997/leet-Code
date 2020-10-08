class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)
        
        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0 
        
#         ls1 = list(version1.strip())
#         ls2 = list(version2.strip())
#         ls1 = self.preprocess(ls1)
#         ls2 = self.preprocess(ls2)
#         ls1 = ("".join(ls1)).split(".")
#         ls2 = ("".join(ls2)).split(".")
        
#         if len(ls1) != len(ls2):
#             ls1 = self.finalProcess(ls1)
#             ls2 = self.finalProcess(ls2)
        
        
#         if len(ls1) >= len(ls2):
#             return self.compare(ls1, ls2)
#         else:
#             status = self.compare(ls2, ls1)
#             if status == 1:
#                 return -1
#             elif status == -1:
#                 return 1
            
#     def finalProcess(self, strList):
#         # print("Final Process")
#         end = len(strList)-1
#         while int(strList[end]) == 0:
#             strList.pop()
#             end -= 1
#         return strList
        
#     def preprocess(self, strList):
#         for i in range(len(strList)):
#             if strList[i] == ".":
#                 start = i+1
#                 while start+1 < len(strList)-1 and strList[start] == "0" and strList[start+1].isdigit():
#                     strList[start] = "#"
#                     start += 1
#         return [s for s in strList if s != "#"]
    
#     def compare(self, list1, list2):
#         # print(list1, list2)
#         i = 0
#         status = 0
#         while i < len(list2):
#             if int(list1[i]) > int(list2[i]):
#                 return 1
#             elif int(list2[i]) > int(list1[i]):
#                 return -1
#             i += 1
#         # print("i: ", i)
#         if i < len(list1):
#             return 1
#         if i < len(list2):
#             return -1
#         return 0
