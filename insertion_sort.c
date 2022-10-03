#include <stdio.h>

/*
Given a sorted list with an unsorted number in the rightmost cell, can you write some simple code to insert e into the array so that it remains sorted?

Assume you are given the array = [1,2,4,5,3] indexed 0...4. Store the value of arr[4].
Now test lower index values successively from 3 to 0 until you reach a value that is lower than arr[4], at arr[1] in this case.
Each time your test fails, copy the value at the lower index to the current index and print your array.
When the next lower indexed value is smaller than arr[4], insert the stored value at the current index and print the entire array.
*/

void printArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%i ", arr[i]);
    }
    printf("\n");
}


void insertionSort1(int n, int arr_count, int* arr) {
    int num = arr[n - 1];
    int i = n - 1;
    while (arr[i - 1] > num && i > 0) {
        arr[i] = arr[i - 1];
        printArray(arr, n);
        i--;
    }
    arr[i] = num;
    printArray(arr, n);
}
