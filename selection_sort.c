int select(int arr[], int i)
{
    int largestEl = i;
    for (int j = i; j >= 0; j-- ) {
        if (arr[j] > arr[largestEl]) {
            largestEl = j;
        }
    }
    return largestEl;
}


void selectionSort(int arr[], int n)
{
  int unsortedIndex = n - 1;
  while (unsortedIndex >= 0) {
      int selectedIndex = select(arr, unsortedIndex);
      int tmp = arr[unsortedIndex];
      arr[unsortedIndex] = arr[selectedIndex];
      arr[selectedIndex] = tmp;
      unsortedIndex--;
  }
}
