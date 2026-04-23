class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prev = []                    
        counter = {}
        holder = {}

        for i, num in enumerate(nums):
            count = counter.get(num, 0)
            cur_sum = holder.get(num, 0)
            prev.append((i * count) + cur_sum)

            counter[num] = counter.get(num, 0) + 1
            holder[num] = holder.get(num, 0) - i
        
        counter.clear()
        holder.clear()

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            count = counter.get(num, 0)
            cur_sum = holder.get(num, 0)
            prev[i] += (-i * count) + cur_sum

            counter[num] = counter.get(num, 0) + 1
            holder[num] = holder.get(num, 0) + i


        return prev
