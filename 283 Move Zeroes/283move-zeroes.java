class Solution {
    private void swapTo(int[] nums, int from, int to) {
        while (from < to) {
            int tmp = nums[from];
            nums[from] = nums[from+1];
            nums[from+1] = tmp;
            from++;
        }
    }
    public void moveZeroes(int[] nums) {
        int last = nums.length - 1;
        int i = 0;

        while (i < last) {
            if (nums[i] == 0) {
                swapTo(nums, i, last);
                last--;
            }
            else {
                i++;
            }
        }
    }
}
