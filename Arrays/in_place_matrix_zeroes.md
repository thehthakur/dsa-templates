## [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`. You must do it **in place**.

### Example 1:

**Input:**  
`matrix = [[1,1,1],[1,0,1],[1,1,1]]`

**Output:**  
`[[1,0,1],[0,0,0],[1,0,1]]`

---

## In-Place Constant Space Approach:

**Idea**: Use the first row and first column of the matrix to store whether a row or column should be zeroed. This allows us to solve the problem in-place with **O(1)** extra space. We need an extra boolean `should_zero_first_row` because `matrix[0][0]` is shared by both the first row and first column. To avoid overwriting their individual zeroing needs, we separately track if the first row should be zeroed.

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        should_zero_first_row: bool = False

        # Step 1: Use first row and column as markers
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        should_zero_first_row = True
                    else:
                        matrix[r][0] = 0

        # Step 2: Zero out cells based on markers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Handle first column separately if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 4: Handle first row based on the flag
        if should_zero_first_row:
            for c in range(COLS):
                matrix[0][c] = 0
```
