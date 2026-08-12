class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0

        for i in range(len(gas)):
            if fuel + gas[i] - cost[i] < 0: #cant reach next station
                start = i + 1 #try starting from next station
                fuel = 0 #reset fuel 
            else: #can reach station
                fuel += gas[i] - cost[i]
        
        return start
