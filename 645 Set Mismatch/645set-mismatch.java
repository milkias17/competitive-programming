class Solution {
    public int[] findErrorNums(int[] nums) {
               int[] countArr = new int[nums.length];
        for (int num: nums) {
            countArr[num - 1]++;
        }

        int missing = 0, duplicate = 0;
        for (int i = 0; i < countArr.length; i++) {
            if (countArr[i] == 0) {
                missing = i + 1;
            }
            if (countArr[i] > 1) {
                duplicate = i + 1;
            }
        }

        int[] res = {duplicate, missing};
        return res;
    }
}