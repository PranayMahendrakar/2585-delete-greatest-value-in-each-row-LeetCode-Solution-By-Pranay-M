class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        result = 0
        for col in range(len(grid[0])):
            max_val = max(row[col] for row in grid)
            result += max_val
        return result