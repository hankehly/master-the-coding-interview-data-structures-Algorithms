from typing import Any, List


class HashTable:
    """
    An implementation of a hash table with `size` slots available.
    If two hashes collide, the next key-value pair is appended to the existing data.

    table = HashTable(10)
    table.set("foo", 10000)
    table.set("bar", 5)
    table.set("hello", 30)
    table.set("hello", 50)
    table.set("world", 19)
    print(table.get("hello"))
    print(table.keys())
    """

    def __init__(self, size: int) -> None:
        self.data = [None] * size

    def _hash(self, key) -> int:
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key: str, value: Any) -> None:
        """
        Sets value of `key` in hash table.
        Handles hash collisions by appending value to current value.
        Time-complexity: O(1)
        """
        addr = self._hash(key)
        if self.data[addr] is None:
            self.data[addr] = []
        # You could handle duplicate keys here, by looping through the data
        # and resetting the appropriate value. But that will make the method O(n)
        # for row in self.data[addr]:
        #     if row[0] == key:
        #         row[1] = value
        #         return
        self.data[addr].append([key, value])

    def get(self, key: str) -> Any:
        """
        Get value of `key` from hash table.
        Gets the value by address, then loops through result until we find a match.
        Time-complexity: O(n)
        """
        addr = self._hash(key)
        item = self.data[addr]
        if item:
            item_len = len(item)
            # Handle duplicate keys by searching in reverse order. This will require
            # more space because the hash table may hold many values for the same key.
            # The other option would be to modify set to loop through each value, which
            # would increase time complexity from O(1) to O(n)
            for i in range(item_len):
                row = item[item_len - 1 - i]
                if row[0] == key:
                    return row[1]
        return None

    def keys(self) -> List[str]:
        """
        Returns the keys (those specified by the programmer) of all the hash table entries.
        Time complexity is BAD O(n^2)
        """
        keys = set()
        for row in filter(None, self.data):
            # The video stops at the following implementation, so it doesn't consider
            # conflicting hashes.
            # keys.add(row[0][0])
            # This is a naive approach to handling conflicting hashes, but may
            # significantly increase time complexity
            for sub_row in row:
                key = sub_row[0]
                keys.add(key)
        return list(keys)


def first_recurring_character(values: List[Any]) -> Any | None:
    """
    first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4])
    => 2
    first_recurring_character([1, 2, 3, 4, 5])
    => None
    """
    seen = {}
    for v in values:
        if seen.get(v):
            return v
        else:
            seen[v] = True
    return None


def main():
    table = HashTable(2)
    table.set("foo", 10)
    table.set("bar", 20)
    table.set("buz", 30)
    table.set("buz", 40)  # has precendence over past value
    assert table.get("bar") == 20
    assert table.get("buz") == 40
    assert sorted(table.keys()) == ["bar", "buz", "foo"]
    assert first_recurring_character([2, 5, 5, 2, 3, 5, 1, 2, 4]) == 5
    assert first_recurring_character([1, 2, 3, 4, 5]) is None


if __name__ == "__main__":
    main()
