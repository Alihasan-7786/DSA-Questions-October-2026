class Solution:
    def canAllocate(self, pages, m, limit):
        groups = 1
        current_pages = 0
        for page in pages:
            if current_pages + page <= limit:
                current_pages += page
            else:
                groups += 1
                current_pages = page

        return groups <= m
    def allocateBooks(self, pages, m):
        n = len(pages)
        if m > n:
            return -1
        left = pages[0]
        right = 0
        for page in pages:
            if page > left:
                left = page
            right += page
        answer = right
        while left <= right:
            mid = (left + right) // 2
            if self.canAllocate(pages, m, mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

n, m = map(int, input().split())
pages = list(map(int, input().split()))

obj = Solution()
print(obj.allocateBooks(pages, m))