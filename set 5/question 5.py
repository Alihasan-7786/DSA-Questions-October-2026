class Solution:
    def findKthLargest(self, arr, k):
        target = len(arr) - k
        left = 0
        right = len(arr) - 1
        while left <= right:
            pivot = arr[(left + right) // 2]
            low = left
            mid = left
            high = right
            while mid <= high:
                if arr[mid] < pivot:
                    arr[low], arr[mid] = arr[mid], arr[low]
                    low += 1
                    mid += 1
                elif arr[mid] > pivot:
                    arr[mid], arr[high] = arr[high], arr[mid]
                    high -= 1
                else:
                    mid += 1
            if target < low:
                right = low - 1
            elif target > high:
                left = high + 1
            else:
                return pivot

n, k = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.findKthLargest(arr, k))