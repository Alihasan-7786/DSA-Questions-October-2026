class Solution:
    def countInversions(self, arr):
        def mergeSort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = mergeSort(left, mid)
            count += mergeSort(mid + 1, right)
            temp = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    count += mid - i + 1
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            for i in range(len(temp)):
                arr[left + i] = temp[i]
            return count
        return mergeSort(0, len(arr) - 1)

n = int(input())
arr = list(map(int, input().split()))

obj = Solution()
print(obj.countInversions(arr))