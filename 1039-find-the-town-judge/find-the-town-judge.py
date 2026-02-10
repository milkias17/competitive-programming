class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return n if n == 1 else -1

        in_degree = {}
        out_degree = {}

        for label, trusted in trust:
            out_degree[label] = out_degree.get(label, 0) + 1
            in_degree[trusted] = in_degree.get(trusted, 0) + 1
            if label not in in_degree:
                in_degree[label] = 0
            if trusted not in out_degree:
                out_degree[trusted] = 0 
        
        # print(in_degree)
        # print(out_degree)
        for person, trust_count in in_degree.items():
            if trust_count == n - 1 and out_degree[person] == 0:
                return person
        
        return -1