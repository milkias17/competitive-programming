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