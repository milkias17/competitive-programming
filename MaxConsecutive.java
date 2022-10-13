import java.util.Arrays;


/* 
    Given a binary array nums and an integer k, return the maximum number
    of consecutive 1's in the array if you can flip at most k 0's.

    Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 
    Output: 6 
    Explanation: [1,1,1,0,0,1,1,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 
    Output:10 
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1] Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
*/

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

        return windowRight - windowLeft;
    }
}

public class MaxConsecutive {
    public static void main(String[] args) {
        Solution sol = new Solution();
        // int[] nums = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
        // int[] nums = {0,0,0,1};
        // int[] nums = {1,1,1,0,0,0,1,1,1,1};
        // int[] nums = {1,1,1,0,0,0,1,1,1,1,0};
        // int[] nums = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
        int[] nums = {1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1};

        System.out.println("Original Array: " + Arrays.toString(nums));
        System.out.println(sol.longestOnes(nums, 8));
    }
}
