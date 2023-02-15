class NumArray {

    int[] prefixSum;
    public NumArray(int[] nums) {
        this.prefixSum = new int[nums.length];
        this.prefixSum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        if (left > 0) {
            return this.prefixSum[right] - this.prefixSum[left - 1];
        }
        return this.prefixSum[right];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */