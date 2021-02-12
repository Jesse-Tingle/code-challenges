import math
#   Returns either the index of the location in the array,
#   or -1 if the array did not contain the targetValue 

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def doSearch(array, targetValue):
    min = 0
    max = len(array) - 1
    guess = math.floor((min+max)/2)


    while (array[guess] != targetValue):
        guess = math.floor((min+max)/2)
        if max < min:
            retun -1
        elif array[guess] < targetValue:
            min = guess + 1
        elif array[guess] > targetValue:
            max = guess - 1
        elif array[guess] == targetValue:
            return guess
            print("You found it!")

result = doSearch(primes, 73)
print(f"Prime found at index {result}")
