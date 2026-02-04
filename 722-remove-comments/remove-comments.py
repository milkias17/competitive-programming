class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        tmp = []
        res = []
        in_comment = False
        for line in source:
            idx = 0
            while idx < len(line):
                if in_comment:
                    if line[idx] == "*" and idx + 1 < len(line) and line[idx + 1] == "/":
                        in_comment = False
                        idx += 2
                    else:
                        idx += 1
                else:
                    if line[idx] == "/" and idx + 1 < len(line) and line[idx + 1] == "/":
                        break
                    if line[idx] == "/" and idx + 1 < len(line) and line[idx + 1] == "*":
                        in_comment = True
                        idx += 2
                    else:
                        tmp.append(line[idx])
                        idx += 1
            
            if not in_comment and len(tmp) > 0:
                res.append("".join(tmp))
                tmp = []

        return res

