class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for i in range(len(logs)):
            if logs[i].split()[1].isalpha():
                letters.append(logs[i])
            else:
                digits.append(logs[i])
                
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])
        
        return letters + digits
