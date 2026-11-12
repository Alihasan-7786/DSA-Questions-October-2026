class Solution:
    def commonMembers(self, A, B):
        setA = set(A)
        seen = set()
        common = []
        for value in B:
            if value in setA and value not in seen:
                common.append(value)
                seen.add(value)
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        return mergeSort(common)

m, n = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

obj = Solution()
answer = obj.commonMembers(A, B)

if len(answer) == 0:
    print("None")
else:
    print(*answer)