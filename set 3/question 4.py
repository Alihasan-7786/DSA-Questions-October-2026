class Solution:
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        return A

m, n = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

obj = Solution()
print(*obj.merge(A, m, B, n))