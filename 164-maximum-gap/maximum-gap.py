class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1

        buckets = [{"min": float("inf"), "max": float("-inf")} for i in range(num_buckets)]

        # print(f"num_buckets: {num_buckets}")
        for num in nums:
            idx = (num - min_val) // bucket_size
            # print(f"idx: {idx}")
            low = buckets[idx]["min"]
            high = buckets[idx]["max"]
            buckets[idx]["min"] = min(low, num)
            buckets[idx]["max"] = max(high, num)
        
        prev = None
        max_gap = float("-inf")
        for bucket in buckets:
            c_min = bucket["min"]
            c_max = bucket["max"]

            if c_min == float("inf"):
                continue

            if prev is None:
                prev = c_max
                continue
            
            max_gap = max(max_gap, c_min - prev)
            prev = c_max


        return max_gap if max_gap != float("-inf") else 0
