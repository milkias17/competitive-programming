class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = []
        for log in logs:
            if log == "../":
                if len(path) >= 1:
                    path.pop()
            elif log == "./":
                continue
            else:
                path.append(log)
        
        return len(path)