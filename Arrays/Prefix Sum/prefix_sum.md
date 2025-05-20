## [Zero Array Transformation I](https://leetcode.com/problems/zero-array-transformation-i/description/)

You are given an integer array `nums` of length `n` and a 2D array `queries`, where `queries[i] = [lᵢ, rᵢ]`.

For each `queries[i]`:

- Select a subset of indices within the range `[lᵢ, rᵢ]` in `nums`.
- Decrement the values at the selected indices by 1.

A **Zero Array** is an array where all elements are equal to `0`.

Return `true` if it is possible to transform `nums` into a Zero Array after processing all the queries sequentially, otherwise return `false`.

---

### Example 1

**Input:**
nums = [1, 0, 1]
queries = [[0, 2]]

**Output:**
true

**Explanation:**

- For `i = 0`:  
  Select the subset of indices as `[0, 2]` and decrement the values at these indices by `1`.  
  The array will become `[0, 0, 0]`, which is a Zero Array.

---

### Approach Explanation

Use a **difference array** (`delta_array`)

#### Key Idea:

- For each query `[start_index, end_index]`, we:
  - Add `+1` at `start_index` in the `delta_array` to **start tracking** allowed operations.
  - Subtract `1` at `end_index + 1` to **end the effect** of the operation range.

> This marks the _start_ and _end_ boundaries of where operations apply. The `+1` represents gaining the right to apply an operation, and the `-1` signifies **losing that right** _after_ the range.

The whole motivation of doing this is so that when we do a **prefix sum** over this difference array you'll always have knowledge of how many operations you can do at a given index.

```python
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta_array: List[int] = [0] * (len(nums) + 1)
        for start_index, end_index in queries:
            delta_array[start_index] += 1
            delta_array[end_index + 1] -= 1

        operation_count: int = 0
        operation_prefix_sum: List[int] = []

        for delta in delta_array:
            operation_count += delta
            operation_prefix_sum.append(operation_count)

        for operations, num in zip(operation_prefix_sum, nums):
            if operations < num:
                return False
        return True
```
