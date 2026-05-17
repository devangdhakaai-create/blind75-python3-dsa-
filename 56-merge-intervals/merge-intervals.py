class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            last = result[-1]
            curr = intervals[i]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                result.append(curr)
        return result