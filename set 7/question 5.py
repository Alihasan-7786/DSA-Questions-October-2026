class Solution:
    def searchMountain(self, arr, h):
        n = len(arr)
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        peak = lo
        lo = 0
        hi = peak
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == h:
                return mid
            elif arr[mid] < h:
                lo = mid + 1
            else:
                hi = mid - 1
        lo = peak + 1
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == h:
                return mid
            elif arr[mid] > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

n = int(input())
arr = list(map(int, input().split()))
h = int(input())

obj = Solution()
print(obj.searchMountain(arr, h))