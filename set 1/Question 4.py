class Solution:
    def balancePoint(self, arr):
        total = 0
        for num in arr:
            total += num
        left = 0
        for i in range(len(arr)):
            right = total - left - arr[i]
            if left == right:
                return i
            left += arr[i]
        return -1


n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.balancePoint(arr))