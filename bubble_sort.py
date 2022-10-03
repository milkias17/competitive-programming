#!/bin/python3

""""
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

    1. Array is sorted in numSwaps swaps where numSwaps is the number of swaps that took place.
    2. First Element: firstElement, where firstElement is the first element in the sorted array.
    3. Last Element: lastElement, where lastElement is the last element in the sorted array.
"""
def countSwaps(a):
    num_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                num_swaps += 1
    
    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
