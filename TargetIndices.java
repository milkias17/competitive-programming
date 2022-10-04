import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

/*
    You are given a 0-indexed integer array nums and a target element
    target.
    A target index is an index i such that nums[i] == target.
    Return a list of the target indices of nums after sorting nums in
    non-decreasing order. If there are no target indices, return an empty
    list. The returned list must be sorted in increasing order.
 **/

class Solution {
    private int[] merge(int[] a, int[] b) {
        int i = 0;
        int j = 0;
        int[] res = new int[a.length + b.length];
        for (int z = 0; z < res.length; z++) {
            if (i >= a.length) {
                res[z] = b[j++];
            } else if (j >= b.length) {
                res[z] = a[i++];
            }
            else {
                if (a[i] < b[j]) {
                    res[z] = a[i++];
                }
                else if (b[j] <= a[i]) {
                    res[z] = b[j++];
                }
            }
        }
        return res;
    }
    private int[] mergeSort(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }
        int mid = (nums.length) / 2;
        int[] leftArr = Arrays.copyOfRange(nums, 0, mid);
        int[] rightArr = Arrays.copyOfRange(nums, mid, nums.length);
        int[] sortedLeft = mergeSort(leftArr);
        int[] sortedRight = mergeSort(rightArr);
        
        return merge(sortedLeft, sortedRight);
    }
    public List<Integer> targetIndices(int[] nums, int target) {
       ArrayList<Integer> result = new ArrayList<Integer>();
       int[] sortedArray = mergeSort(nums);
       for (int i = 0; i < sortedArray.length; i++) {
           if (sortedArray[i] == target) {
               result.add(i);
           }
       }
       return result; 
    }
}
