class Solution:
    def reverse(self, arr: List, start_index: int, end_index: int):
        while start_index < end_index:
            arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
            start_index += 1
            end_index -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
