def search_quadruplets(arr, target):
  arr.sort()
  quadruplets = []
  # TODO: Write your code here
  for i in range(0, len(arr)-3):
    # To avoid duplicates
    if i > 0 and arr[i] == arr[i+1]:
      continue
    for j in range(i+1, len(arr)-2):
      # To avoid duplicates
      if j > i+1 and arr[j] == arr[j-1]:
        continue
      left = j+1
      right = len(arr)-1
      while left < right:
        currentSum = arr[i] + arr[j] + arr[left] + arr[right]
        if currentSum == target:
          quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
          left += 1
          right -= 1
          # To avoid duplicates
          while (left < right and arr[left] == arr[left-1]):
            left += 1
          # TO avoid duplicates
          while (left < right and arr[right] == arr[right+1]):
            right -= 1
        elif currentSum < target:
          left += 1
        else:
          right -= 1


  return quadruplets
