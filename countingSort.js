/*
  Another sorting method, the counting sort, does not require comparison. 
  Instead, you create an integer array whose index range covers the entire range of values in your array to sort.
  Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, 
  printing the value of each non-zero valued index that number of times.
*/
function countingSort(arr) {
  let result = [];
  for (let i = 0; i < 100; i++) {
    result[i] = 0;
  }
  for (let i = 0; i < arr.length; i++) {
    result[arr[i]] += 1;
  }
  return result;
}
