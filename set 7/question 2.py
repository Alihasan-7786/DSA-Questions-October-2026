class Solution:
    def searchInsert(self, arr, t):
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == t:
                return mid
            elif arr[mid] < t:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

n = int(input())
arr = list(map(int, input().split()))
t = int(input())

obj = Solution()
print(obj.searchInsert(arr, t))