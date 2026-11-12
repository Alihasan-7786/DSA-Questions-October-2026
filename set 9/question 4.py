class Solution:
    def mergeSort(self, intervals):
        if len(intervals) <= 1:
            return intervals
        mid = len(intervals) // 2
        left = self.mergeSort(intervals[:mid])
        right = self.mergeSort(intervals[mid:])
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def mergeIntervals(self, intervals):
        intervals = self.mergeSort(intervals)
        merged = []
        for start, end in intervals:
            if len(merged) == 0 or start > merged[-1][1]:
                merged.append([start, end])
            else:
                if end > merged[-1][1]:
                    merged[-1][1] = end

        return merged

n = int(input())
intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

obj = Solution()
answer = obj.mergeIntervals(intervals)

for start, end in answer:
    print(start, end)