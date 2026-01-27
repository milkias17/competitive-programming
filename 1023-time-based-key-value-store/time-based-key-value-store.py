class TimeMap:

    def __init__(self):
        self._data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._data:
            tmp = [(timestamp, value)]
            self._data[key] = tmp
        else:
            self._data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._data:
            return ""
        
        arr = self._data[key]
        res = ""
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)