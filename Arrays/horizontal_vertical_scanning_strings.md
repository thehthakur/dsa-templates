## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

Write a function to find the **longest common prefix** string amongst an array of strings.  
If there is no common prefix, return an empty string `""`.

### Example 1:

**Input:**  
`strs = ["flower", "flow", "flight"]`

**Output:**  
`"fl"`

## Horizontal Scanning:

```python
def longestCommonPrefix(strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix: str = strs[0]
        for i in range(1, len(strs)):
            # keep shrinking the prefix string from the end till we get a prefix match
            while strs[i].find(prefix) != 0: # Horizontal Scanning Step: I'm comparing all elements of two strings
                prefix = prefix[0 : len(prefix) - 1]
                # exit if shrinking the prefix string makes it empty
                if prefix == "":
                    return ""
        return prefix
```

## Vertical Scanning:

```python
def longestCommonPrefix(strs: List[str]) -> str:
    if strs == None or len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        # Check the ith character of each string first, then move on
        # Lets us optimize by doing an early return if the list contains a very short string
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]
```
