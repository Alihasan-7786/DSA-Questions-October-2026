class Solution:
    def mergeLists(self, A, B):
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                value = A[i]
                i += 1
            elif A[i] > B[j]:
                value = B[j]
                j += 1
            else:
                value = A[i]
                i += 1
                j += 1
            if not result or result[-1] != value:
                result.append(value)
        while i < len(A):
            if not result or result[-1] != A[i]:
                result.append(A[i])
            i += 1
        while j < len(B):
            if not result or result[-1] != B[j]:
                result.append(B[j])
            j += 1
        return result

m, n = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

obj = Solution()
print(*obj.mergeLists(A, B))