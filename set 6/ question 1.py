class Solution:
    def countingSort(self, arr):
        count = [0] * 101
        for mark in arr:
            count[mark] += 1
        result = []
        for mark in range(101):
            for i in range(count[mark]):
                result.append(mark)
        return result

n = int(input())
arr = list(map(int, input().split()))
obj = Solution()
result = obj.countingSort(arr)

print(*result)