class Solution:
    def findMissing(self, arr):
        n = len(arr)
        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] > 0:
                arr[index] = -arr[index]
        result = []
        for i in range(n):
            if arr[i] > 0:
                result.append(i + 1)
        return result
n = int(input())
arr = list(map(int, input().split()))
obj = Solution()
result = obj.findMissing(arr)

if result:
    print(*result)
else:
    print("None")