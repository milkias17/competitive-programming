import java.util.Arrays;

/* 
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.

    Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Example 2:
    Input: nums = [0]
    Output: [0] 
*/


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

public class MoveZeroes {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {0,1,0,3,12};
        sol.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}
