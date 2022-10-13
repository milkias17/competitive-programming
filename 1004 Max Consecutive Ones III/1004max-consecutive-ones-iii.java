class Solution {
      
    public int longestOnes(int[] nums, int k) {
        int windowLeft = 0;
        int windowRight = 0;

        for (; windowRight < nums.length; windowRight++) {
            if (nums[windowRight] == 0) {
                k--;
            }

            if (k < 0) {
                if (nums[windowLeft] == 0) {
                    k++;
                }
                windowLeft++;
            }
        }

        return (windowRight - windowLeft);
    }
}