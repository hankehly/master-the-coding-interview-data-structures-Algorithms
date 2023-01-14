import logging
import os
from typing import Any

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node = None
        self.prev: Node = None


class StackBuiltWithLinkedList:
    """
    An implementation of a Stack using a doubly linked list.

    You could instantiate a doubly linked list from section 8 and reuse the methods here,
    but all we really need is the "Node" class which stores value, next, and prev values.

    self._top and self._bottom are our "head" and "tail"
    """

    def __init__(self) -> None:
        self._top: Node = None
        self._bottom: Node = None
        self._length = 0

    @property
    def empty(self) -> bool:
        return self._length == 0

    def peek(self) -> Any:
        return self._top.value

    def push(self, value: Any) -> None:
        node = Node(value)
        if self.empty:
            self._top = node
            self._bottom = node
            self._length = 1
        else:
            # place the new node at the front of the stack
            # and link it to the next element
            old_top = self._top
            old_top.prev = node
            node.next = old_top
            self._top = node
            self._length += 1

    def pop(self) -> Any:
        if self.empty:
            return None
        # If this stack only has 1 item, the top and bottom pointers will
        # both be null at the end of the operation. We update top below,
        # so update bottom here.
        if self._top == self._bottom:
            self._bottom = None
        old_top = self._top
        self._top = self._top.next
        if self._top:
            self._top.prev = None
        # We could also update the bottom here, because if top is None,
        # bottom should also be None
        # else:
        #     self._bottom = None
        self._length -= 1
        return old_top.value


class StackBuiltWithArray:
    def __init__(self) -> None:
        self._data = []

    @property
    def empty(self) -> bool:
        return len(self._data) == 0

    def peek(self) -> Any:
        if self.empty:
            return None
        return self._data[-1]

    def push(self, value: Any) -> None:
        logging.debug(f"[push] Pushing {value} onto the stack.")
        self._data.append(value)

    def pop(self) -> Any:
        if self.empty:
            return None
        value = self._data.pop()
        logging.debug(
            f"[pop] Popped {value} from the stack. Length is now {len(self._data)}."
        )
        return value


def main():
    # stack = StackBuiltWithLinkedList()
    stack = StackBuiltWithArray()
    stack.push("google")
    stack.push("udemy")
    stack.push("discord")
    assert not stack.empty
    assert stack.peek() == "discord"
    assert stack.pop() == "discord"
    assert stack.pop() == "udemy"
    assert stack.pop() == "google"
    assert stack.empty
    assert stack.pop() is None


if __name__ == "__main__":
    main()
