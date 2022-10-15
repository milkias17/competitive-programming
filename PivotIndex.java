/* 
   Given an array of integers nums, calculate the pivot index of this

   array.
   The pivot index is the index where the sum of all the numbers
   strictly to the left of the index is equal to the sum of all the
   numbers strictly to the index's right.

   If the index is on the left edge of the array, then the left sum is
   0 because there are no elements to the left. This also applies to
   the right edge of the array.

   Return the leftmost pivot index. If no such index exists, return -1.
*/

class Solution {
    public int pivotIndex(int[] nums) {
        int[] leftPrefixSum = new int[nums.length];
        int[] rightPrefixSum = new int[nums.length];

        leftPrefixSum[0] = nums[0];
        rightPrefixSum[nums.length - 1] = nums[nums.length - 1];

        for (int i = 1; i < nums.length; i++) {
            leftPrefixSum[i] = leftPrefixSum[i - 1] + nums[i];
        }

        for (int i = nums.length - 2; i >= 0; i--) {
            rightPrefixSum[i] = rightPrefixSum[i + 1] + nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            int leftSum;
            int rightSum;
            if (i == 0) {
                leftSum = 0;
            } else {
                leftSum = leftPrefixSum[i - 1];
            }

            if (i == nums.length - 1) {
                rightSum = 0;
            } else {
                rightSum = rightPrefixSum[i + 1];
            }

            if (leftSum == rightSum) {
                return i;
            }
        }

        return -1;
        
    }
}
