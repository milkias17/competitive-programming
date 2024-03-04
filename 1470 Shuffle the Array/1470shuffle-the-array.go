func shuffle(nums []int, n int) []int {
    var newNums []int
    left, right := 0, n

    for left < n * 2 && right < n * 2 {
        if left < n * 2 {
            newNums = append(newNums, nums[left])
        }
        if right < n * 2 {
            newNums = append(newNums, nums[right])
        }
        left++
        right++
    }
    return newNums
}