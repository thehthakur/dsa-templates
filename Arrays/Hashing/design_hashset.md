# [Design HashSet](https://leetcode.com/problems/design-hashset/description/)

Design a HashSet without using any built-in hash table libraries.

Implement the `MyHashSet` class:

- `void add(key)` → Inserts the value `key` into the HashSet.
- `bool contains(key)` → Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` → Removes the value `key` in the HashSet. If `key` does not exist, do nothing.

## Example 1:

**Input:**

```
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
```

**Output:**

```
[null, null, null, true, false, null, true, null, false]
```

**Explanation:**

```python
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      # set = [1]
myHashSet.add(2);      # set = [1, 2]
myHashSet.contains(1); # return True
myHashSet.contains(3); # return False (not found)
myHashSet.add(2);      # set = [1, 2]
myHashSet.contains(2); # return True
myHashSet.remove(2);   # set = [1]
myHashSet.contains(2); # return False (already removed)
```

## Constraints:

- `0 <= key <= 10^6`
- At most `10^4` calls will be made to `add`, `remove`, and `contains`

---

## HashSet Implementation (Chaining with Doubly Linked List + Multiplication Hashing)

```python
import math

class Node:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None

    def search(self, val: int) -> Node | None:
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None

    def insert(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        if self.search(val):  # avoid duplicates
            return

        curr_first_node: Node = self.head
        new_node: Node = Node(val, None, curr_first_node)
        curr_first_node.prev = new_node

        # Update head
        self.head = new_node

    def delete(self, val: int) -> None:
        node = self.search(val)
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        del node


class MyHashSet:
    A: float = (math.sqrt(5) - 1) / 2  # Multiplication method constant
    m: int = 2**10  # Table size (power of 2)

    def __init__(self):
        self.hashset: list[DoublyLinkedList | None] = [None for _ in range(self.m)]

    def add(self, key: int) -> None:
        index = self.hash_function(key)
        if not self.hashset[index]:
            self.hashset[index] = DoublyLinkedList()
        self.hashset[index].insert(key)

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        if self.hashset[index]:
            self.hashset[index].delete(key)

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        return bool(self.hashset[index] and self.hashset[index].search(key))

    def hash_function(self, key: int) -> int:
        return math.floor(self.m * ((key * self.A) % 1))
```
