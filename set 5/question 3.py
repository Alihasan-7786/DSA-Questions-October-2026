class Solution:
    def insertionSort(self, arr):
        shifts = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            arr[j + 1] = key
        return arr, shifts

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
result, shifts = obj.insertionSort(arr)

print(*result)
print(shifts)