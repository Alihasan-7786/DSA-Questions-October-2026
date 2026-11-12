class Solution:
    def moveZeroes(self, arr):
        index = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[index] = arr[i]
                index += 1
        while index < len(arr):
            arr[index] = 0
            index += 1
        return arr

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(*obj.moveZeroes(arr))