def search_quadruplets(arr, target):
  arr.sort()
  quadruplets = []
  # TODO: Write your code here
  for i in range(len(arr)-3):
    for j in range(i+1, len(arr)-2):
      left = j+1
      right = len(arr)-1
      while left < right:
        currentSum = arr[i] + arr[j] + arr[left] + arr[right]
        if currentSum == target:
          quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
          break
        elif currentSum < target:
          left += 1
        else:
          right -= 1


  return quadruplets
