class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        peopleDict, height, res = {}, [], []
        
        for i in range(len(people)):
            p = people[i]
            if p[0] not in peopleDict:
                peopleDict[p[0]] = [(p[1], i)]
                height.append(p[0])
            else:
                peopleDict[p[0]] += [(p[1], i)]
                
        height.sort()
        
        for h in height[::-1]:
            peopleDict[h].sort()
            for p in peopleDict[h]:
                res.insert(p[0], people[p[1]])
        
        return res
