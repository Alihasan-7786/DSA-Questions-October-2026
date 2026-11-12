class Solution:
    def fastestDeliveries(self, arr, k):
        n = len(arr)
        for i in range(k):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr[:k]

n, k = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(*obj.fastestDeliveries(arr, k))