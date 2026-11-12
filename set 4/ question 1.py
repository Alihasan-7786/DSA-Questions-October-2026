class Solution:
    def maxWindowSum(self, arr, k):
        total = 0
        for i in range(k):
            total += arr[i]
        maximum = total
        for i in range(k, len(arr)):
            total = total + arr[i] - arr[i - k]
            if total > maximum:
                maximum = total
        return maximum

n, k = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.maxWindowSum(arr, k))