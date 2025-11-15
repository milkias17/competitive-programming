class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            try:
                record.append(int(operation))
            except ValueError:
                if operation == "+":
                    record.append(record[-1] + record[-2])
                elif operation == "D":
                    record.append(record[-1] * 2)
                elif operation == "C":
                    record.pop()
        
        return sum(record)