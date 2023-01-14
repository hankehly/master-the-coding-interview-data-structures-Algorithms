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

    self.top and self.bottom are our "head" and "tail"
    """

    def __init__(self) -> None:
        self.top: Node = None
        self.bottom: Node = None
        self.length = 0

    @property
    def empty(self) -> bool:
        return self.length == 0

    def peek(self) -> Any:
        return self.top.value

    def push(self, value: Any) -> None:
        node = Node(value)
        if self.empty:
            self.top = node
            self.bottom = node
            self.length = 1
        else:
            # place the new node at the front of the stack
            # and link it to the next element
            old_top = self.top
            old_top.prev = node
            node.next = old_top
            self.top = node
            self.length += 1

    def pop(self) -> Any:
        if self.empty:
            return None
        # If this stack only has 1 item, the top and bottom pointers will
        # both be null at the end of the operation. We update top below,
        # so update bottom here.
        if self.top == self.bottom:
            self.bottom = None
        old_top = self.top
        self.top = self.top.next
        if self.top:
            self.top.prev = None
        # We could also update the bottom here, because if top is None,
        # bottom should also be None
        # else:
        #     self.bottom = None
        self.length -= 1
        return old_top.value


class StackBuiltWithArray:
    def __init__(self) -> None:
        self.data = []

    @property
    def empty(self) -> bool:
        return self.length == 0

    @property
    def length(self) -> int:
        return len(self.data)

    @property
    def top(self) -> Node:
        if self.empty:
            return None
        return self.data[-1]

    @property
    def bottom(self) -> Node:
        if self.empty:
            return None
        return self.data[0]

    def peek(self) -> Any:
        return self.top.value

    def push(self, value: Any) -> None:
        logging.debug(f"[push] Pushing {value} on the stack")
        new_node = Node(value)
        self.data.append(new_node)

    def pop(self) -> Any:
        if self.empty:
            return None
        node = self.data.pop()
        logging.debug(
            f"[pop] Popped {node.value} from stack. Length is now {len(self.data)}"
        )
        return node.value


def main():
    # stack = StackBuiltWithLinkedList()
    stack = StackBuiltWithArray()
    stack.push("google")
    stack.push("udemy")
    stack.push("discord")
    assert not stack.empty
    assert stack.top.value == "discord"
    assert stack.bottom.value == "google"
    assert stack.peek() == "discord"
    assert stack.pop() == "discord"
    assert stack.pop() == "udemy"
    assert stack.top.value == "google"
    assert stack.pop() == "google"
    assert stack.empty
    assert stack.pop() is None
    assert stack.top is None
    assert stack.bottom is None


if __name__ == "__main__":
    main()
