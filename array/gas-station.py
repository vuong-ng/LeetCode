class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        total_gain = 0
        res = 0
        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            if total_gain < 0:
                total_gain = 0
                res = i+1
        return res


        