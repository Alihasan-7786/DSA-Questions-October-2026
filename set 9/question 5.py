
class Solution:
    def insertBooking(self, intervals, newBooking):
        result = []
        start, end = newBooking
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= end:
            if intervals[i][0] < start:
                start = intervals[i][0]
            if intervals[i][1] > end:
                end = intervals[i][1]
            i += 1
        result.append([start, end])
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

n = int(input())
intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

newBooking = list(map(int, input().split()))

obj = Solution()
answer = obj.insertBooking(intervals, newBooking)

for start, end in answer:
    print(start, end)