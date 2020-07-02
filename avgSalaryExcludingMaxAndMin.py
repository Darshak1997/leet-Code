class Solution:
    def average(self, salary: List[int]) -> float:
        # O(n)
        max, min = -inf, inf
        for i in range(len(salary)):
            if salary[i] > max:
                max = salary[i]
            if salary[i] < min:
                min = salary[i]
        # print(max, min)
        sum = 0
        for i in range(len(salary)):
            if salary[i] == max or salary[i] == min:
                continue
            else:
                # print(salary[i])
                sum += salary[i]
        return sum/(len(salary)-2)
        
        
        # O(nlogn)
        # salary.sort()
        # salary = salary[1:len(salary)-1]
        # # print(salary)
        # return sum(salary)/len(salary)
