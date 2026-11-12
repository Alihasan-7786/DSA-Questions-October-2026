class Solution:
    def searchMatrix(self, matrix, R, C, t):
        lo = 0
        hi = R * C - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row = mid // C
            col = mid % C
            if matrix[row][col] == t:
                return row, col
            elif matrix[row][col] < t:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1, -1

R, C = map(int, input().split())

matrix = []
for i in range(R):
    matrix.append(list(map(int, input().split())))

t = int(input())

obj = Solution()
row, col = obj.searchMatrix(matrix, R, C, t)
print(row, col)