class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        new_responses = []
        counter = {}
        for response in responses:
            tmp = list(set(response))
            for val in tmp:
                counter[val] = counter.get(val, 0 ) + 1
        
        max_resp = None
        for resp, count in counter.items():
            if max_resp is None:
                max_resp = resp
            elif counter[max_resp] < count:
                max_resp = resp
            elif counter[max_resp] == count:
                max_resp = min(max_resp, resp)
        
        return max_resp
