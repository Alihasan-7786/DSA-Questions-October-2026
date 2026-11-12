class Solution:
    def quickSort(self, arr):
        stack = [(0, len(arr) - 1)]
        while stack:
            left, right = stack.pop()
            if left >= right:
                continue
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
            stack.append((left, low - 1))
            stack.append((high + 1, right))

        return arr

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(*obj.quickSort(arr))