class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #if new end < curr start (not overlapping)
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]: #if new start > curr end
                output.append(intervals[i])
            else: #merge
                newInterval = [min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])]
        
        #if there were no overlapping intervals, add to end
        output.append(newInterval)

        return output