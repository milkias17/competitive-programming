class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        count = 0
        count += sum(cost[0] for cost in costs[:n])
        count += sum(cost[1] for cost in costs[n:])
        return count