"""
Dynamic Array Implementation - Revision Notes & Edge Cases
   - Shrinking bounds: When copying elements to a new array during a downsize, only loop up to `self._size`, NOT `self.capacity`.
   - Capacity collapse: Enforce a MINIMUM_CAPACITY. If you continuously halve the capacity without a floor, it will eventually reach 0, permanently breaking the array.
   - Shrink condition logic: When evaluating if the array should shrink, check if `self.capacity > self.MINIMUM_CAPACITY`, NOT if the `self._size` is greater than the minimum.
     Checking the size causes a bug where the capacity gets stuck at a massive size forever.

2. Edge Cases & Boundary Safety:
   - Empty arrays: Always check `if self._size == 0` in `pop_back()` to prevent the size from becoming negative and corrupting the state.
   - Strict index validation: Any method that accepts an index (`get`, `set`, `insert`, `pop`) must validate it. Remember that for `insert`, `index == self._size` is valid, but for `get`, `set`, and `pop`, it is out of bounds.

3. Performance & Efficiency ("Gotchas"):
   - Native Initialization: Use `array("i", [0]) * capacity` instead of a list comprehension like `[0 for _ in range(capacity)]`.
   - Internal Redundancy: Inside internal loops (like `contains`, `remove`, or `pop`), access `self.fixed_array[i]` directly.
     Calling `self.get(i)` and `self.set(i)` inside a loop forces the program to re-evaluate the boundary `if index < 0...` check on every single iteration, destroying performance.
   - Shifting > Swapping: When inserting into the middle of an array, shift the existing elements to the right in one pass.
     Appending to the end and swapping elements backward is computationally heavier.

4. API Design Best Practices:
   - Ambiguous returns: If `remove(x)` fails to find `x`, raise a `ValueError`. Returning `-1` is dangerous because `-1` could be a valid integer stored inside the array, leaving the user guessing if it was removed or not found.
   - Constants: Define constants (like `MINIMUM_CAPACITY`) at the class level, not inside instance initialization.
"""

from array import array


class DynamicArray:
    MINIMUM_CAPACITY = 16

    def __init__(self) -> None:
        self.capacity = self.MINIMUM_CAPACITY
        self._size = 0
        self.fixed_array = array("i", [0]) * self.capacity

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        return self.fixed_array[index]

    def set(self, index: int, x: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        self.fixed_array[index] = x

    def size(self) -> int:
        return self._size

    def append(self, x: int) -> None:
        if self._size == self.capacity:
            self.resize(self.capacity * 2)

        self.fixed_array[self._size] = x
        self._size += 1

    def pop_back(self) -> None:
        if self._size == 0:
            raise IndexError("Popping from empty array")

        self._size -= 1

        if self.capacity > self.MINIMUM_CAPACITY and self._size <= 0.25 * self.capacity:
            self.resize(max(self.capacity // 2, self.MINIMUM_CAPACITY))

    def resize(self, new_capacity: int) -> None:
        if new_capacity == self.capacity:
            return

        resized_array = array("i", [0]) * new_capacity

        for i in range(self._size):
            resized_array[i] = self.fixed_array[i]

        self.capacity = new_capacity
        self.fixed_array = resized_array

    def pop(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        num_to_remove: int = self.fixed_array[index]

        for i in range(index, self._size - 1):
            self.fixed_array[i] = self.fixed_array[i + 1]

        self.pop_back()
        return num_to_remove

    def contains(self, x: int) -> bool:
        for i in range(self._size):
            if self.fixed_array[i] == x:
                return True
        return False

    def insert(self, index: int, x: int) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if self._size == self.capacity:
            self.resize(self.capacity * 2)

        for i in range(self._size, index, -1):
            self.fixed_array[i] = self.fixed_array[i - 1]

        self.fixed_array[index] = x
        self._size += 1

    def remove(self, x: int) -> None:
        for i in range(self._size):
            if self.fixed_array[i] == x:
                self.pop(i)
                return

        raise ValueError("Value not found in array")
