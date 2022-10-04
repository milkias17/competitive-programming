/*
    Given an array nums with n objects colored red, white, or blue, sort
    them in-place so that objects of the same color are adjacent, with the
    colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white,
    and blue, respectively.

    You must solve this problem without using the library's sort function.
**/
class Solution {
    private void bubbleSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                if (nums[i] < nums[j]) {
                    swap(nums, i, j);
                }
            }
        }
    }
    private void swap(int[] nums, int index1, int index2) {
        int tmp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = tmp;
    }

    public void sortColors(int[] nums) {
        bubbleSort(nums);
    }
}
