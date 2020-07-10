def meandering(arr):
    res = []
    n = len(arr)
    arr.sort()
    i = 0
    j = n - 1
    while i < j:
        print("j: ", arr[j])
        res.append(arr[j])
        j -= 1
        res.append(arr[i])
        i += 1
        print(arr)
    if (n%2 != 0):
        res.append(arr[i])
    if res[-1] == res[-2]:
        res.pop()
    print(res)

arr = [7, 5, 2, 7, 8, -2, 25, 25, 5, 5, ] 
meandering(arr)

friends = ["1100", "0110", "0001", "1000"]

def grid(friends):
    n = len(friends)
    res = [[0] * n] * n
    print(res)

    

grid(friends)
