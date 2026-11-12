class Solution:
    def countStrongDays(self, arr, k, T):
        total = 0
        for i in range(k):
            total += arr[i]
        count = 0
        if total >= k * T:
            count += 1
        for i in range(k, len(arr)):
            total = total + arr[i] - arr[i - k]
            if total >= k * T:
                count += 1
        return count

n, k, T = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.countStrongDays(arr, k, T))