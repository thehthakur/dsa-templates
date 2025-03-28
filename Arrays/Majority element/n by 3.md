# [Majority Element II](https://leetcode.com/problems/majority-element-ii/description/)

Given an integer array of size _n_, find all elements that appear more than ⌊ _n_/3 ⌋ times.

---

## Example 1:

**Input:**  
`nums = [3,2,3]`  
**Output:**  
`[3]`

## Example 2:

**Input:**  
`nums = [1]`  
**Output:**  
`[1]`

## Example 3:

**Input:**  
`nums = [1,2]`  
**Output:**  
`[1,2]`

---

## Constraints:

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

---

### Requirement:

Solve the problem in **linear time** and in **O(1) space**

```python
def extended_boyer_moore(nums: List[int]) -> List[int]:
    """
    Find elements that appear more than ⌊n/3⌋ times in the given list.

    Args:
        nums (List[int]): Input list of integers

    Returns:
        List[int]: List of elements appearing more than ⌊n/3⌋ times
    """
    if not nums:
        return []

    # Initialize candidates and their counts
    candidate1: Optional[int] = None
    candidate2: Optional[int] = None
    count1: int = 0
    count2: int = 0

    # First pass: Find potential candidates
    for num in nums:
        # First priority: Increment count
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        # Second priority: Handle case where count == 0
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        # Third priority: Decrement count
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: Count occurrences of candidates
    threshold: int = len(nums) // 3
    result: List[int] = []

    for candidate in (candidate1, candidate2):
        if candidate is not None and nums.count(candidate) > threshold:
            result.append(candidate)

    # Uncomment the following line
    # If it is reuiqred to sort the answer array
    # result.sort()

    return result


if __name__ == "__main__":
    nums: List[int] = [11, 33, 33, 11, 33, 11]

    ans: List[int] = extended_boyer_moore(nums)
    print(ans)
```
