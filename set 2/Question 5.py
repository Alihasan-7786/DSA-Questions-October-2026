class Solution:
    def rotate(self, arr, k):
        n = len(arr)
        k = k % n
        def reverse(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return arr


n, k = map(int, input().split())
arr = list(map(int, input().split()))

obj = Solution()
print(*obj.rotate(arr, k))