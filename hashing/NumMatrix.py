class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefixSum = []
            return
        rows, cols = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                self.prefixSum[i][j] = matrix[i][j]
                if i > 0:
                    self.prefixSum[i][j] += self.prefixSum[i - 1][j]
                if j > 0:
                    self.prefixSum[i][j] += self.prefixSum[i][j - 1]
                if i > 0 and j > 0:
                    self.prefixSum[i][j] -= self.prefixSum[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        if not self.prefixSum:
            return 0
        total = self.prefixSum[row2][col2]
        if row1 > 0:
            total -= self.prefixSum[row1 - 1][col2]
        if col1 > 0:
            total -= self.prefixSum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += self.prefixSum[row1 - 1][col1 - 1]
        return total


# Example usage:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

# Create NumMatrix object
obj = NumMatrix(matrix)

# Query a region sum
result = obj.sumRegion(2, 1, 4, 3)  # Expected output: 8

print("Sum of region (2,1) to (4,3):", result)
