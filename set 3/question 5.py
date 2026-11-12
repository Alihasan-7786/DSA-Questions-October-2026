class Solution:
    def removeDuplicates(self, arr):
        if len(arr) <= 2:
            return len(arr)
        index = 2
        for i in range(2, len(arr)):
            if arr[i] != arr[index - 2]:
                arr[index] = arr[i]
                index += 1
        return index

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
k = obj.removeDuplicates(arr)

print(k)
print(*arr[:k])