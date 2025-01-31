class Solution:
    def merge(self, intervals):
        # [[1,3],[2,6],[8,10],[15,18]]
        # current start = 1
        # current end = 3

        # if next start <= current end
        # current end = max(new.end, current.end)

        # if next start > current end
        # commit and current start == new start and current end == new end

        # sort
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        current_start = intervals[0][0]
        current_end = intervals[0][1]

        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            new_end = intervals[i][1]

            if new_start <= current_end:
                current_end = max(new_end, current_end)
            else:
                result.append([current_start, current_end])
                current_start = new_start
                current_end = new_end
        result.append([current_start, current_end])
        return result