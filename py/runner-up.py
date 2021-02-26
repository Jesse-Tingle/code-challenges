def runnerUp(arr):
  newArr = []
  # loop through numbers
  for i in arr:
      # remove duplicates
      if i not in newArr:
          # only adds uniqe numbers to new array
          newArr.append(i)
          
  # sorts array in accending order
  newArr.sort()

  # prints second to last number in newArray
  print(newArr[-2])

runnerUp([2, 3, 6, 6, 5])