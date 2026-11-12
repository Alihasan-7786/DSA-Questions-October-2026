class Solution:
    def search(self, arr, t):
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == t:
                return mid
            if arr[lo] <= arr[mid]:
                if arr[lo] <= t < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if arr[mid] < t <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

n = int(input())
arr = list(map(int, input().split()))
t = int(input())

obj = Solution()
print(obj.search(arr, t))