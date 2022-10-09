/* 
    You are given an integer array height of length n. There are n vertical
    lines drawn such that the two endpoints of the ith line are (i, 0) and
    (i, height[i]).

    Find two lines that together with the x-axis form a container, such that
    the container contains the most water.

    Return the maximum amount of water a container can store.
*/

class Solution {
    public int maxArea(int[] height) {
        int resArea = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int currentArea = 0;
            if (height[left] < height[right]) {
                currentArea = height[left] * (right - left);
            }
            else {
                currentArea = height[right] * (right - left);
            }
            if (resArea < currentArea) {
                resArea = currentArea;
            }

            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }
       return resArea;

    }
}

public class MaxContainer {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] height = {1,8,6,2,5,4,8,3,7};
        // int[] height = {1, 1};
        System.out.println(sol.maxArea(height));
    }
}
