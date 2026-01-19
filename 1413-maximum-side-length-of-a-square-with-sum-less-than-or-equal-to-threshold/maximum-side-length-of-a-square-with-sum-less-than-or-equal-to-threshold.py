class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Prefix sum matrix
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (
                    mat[i-1][j-1]
                    + pre[i-1][j]
                    + pre[i][j-1]
                    - pre[i-1][j-1]
                )

        # Binary search for max side length
        left, right = 0, min(m, n)

        while left < right:
            mid = (left + right + 1) // 2
            found = False

            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    square_sum = (
                        pre[i+mid][j+mid]
                        - pre[i][j+mid]
                        - pre[i+mid][j]
                        + pre[i][j]
                    )
                    if square_sum <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                left = mid
            else:
                right = mid - 1

        return left
