# [Majority Element](https://leetcode.com/problems/majority-element/description/)

Given an array `nums` of size `n`, return the majority element.

The **majority element** is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

## Example 1:

**Input:**  
`nums = [3,2,3]`

**Output:**  
`3`

## Example 2:

**Input:**  
`nums = [2,2,1,1,1,2,2]`

**Output:**  
`2`

## Constraints:

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

**Requirement:** Solve the problem in **linear time** and in **O(1) space**?

**Boyer–Moore Majority Voting Algorithm**

```python
def majorityElement(nums: List[int]) -> int:
    candidate: Optional[int] = None
    count: int = 0

    for num in nums:
        if count == 0:
            candidate = num
        # increment count if num == candidate, decrement it otherwise
        count += (1 if num == candidate else -1)

    # Verify that candidate is actually a majority element
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1
```
