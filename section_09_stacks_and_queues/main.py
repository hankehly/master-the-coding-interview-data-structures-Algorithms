import logging
import os
from typing import Any

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node = None

    def __str__(self) -> str:
        return str(self.value)


class StackBuiltWithLinkedList:
    """
    An implementation of a Stack using a linked list.

    You could instantiate a linked list from section 8 and reuse the methods here,
    but all we really need is the "Node" class which stores value and next values.

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
            # To make this a doubly linked list, also set the prev attribute.
            # old_top.prev = node
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
        # To make this a doubly linked list, also set the prev attribute.
        # if self._top:
        #     self._top.prev = None
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


class Queue:
    """
    An implementation of a queue using a singly linked list
    """

    def __init__(self) -> None:
        self._first: Node = None
        self._last: Node = None
        self._length = 0

    @property
    def empty(self) -> bool:
        return self._length == 0

    def peek(self) -> Any:
        if self.empty:
            return None
        return self._first.value

    def enqueue(self, value: Any) -> None:
        logging.debug(f"[enqueue] {value}, length {self._length} -> {self._length + 1}")
        new_node = Node(value)
        if self.empty:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._length += 1

    def dequeue(self) -> Any:
        if self.empty:
            return None
        old_first = self._first
        new_first = self._first.next
        logging.debug(
            f"[dequeue] {old_first} length {self._length} -> {self._length - 1}, "
            f"first {old_first} -> {new_first}"
        )
        self._first = new_first
        self._length -= 1
        return old_first.value


def main():
    stack1 = StackBuiltWithLinkedList()
    stack2 = StackBuiltWithArray()
    for stack in (stack1, stack2):
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

    queue = Queue()
    assert queue.empty
    assert queue.peek() is None
    queue.enqueue("Joy")
    assert queue.peek() == "Joy"
    assert not queue.empty
    queue.enqueue("Matt")
    assert queue.peek() == "Joy"
    queue.enqueue("Pavel")
    queue.enqueue("Samir")
    assert queue.dequeue() == "Joy"
    assert queue.peek() == "Matt"
    assert queue.dequeue() == "Matt"
    assert queue.dequeue() == "Pavel"
    assert queue.dequeue() == "Samir"
    assert queue.empty
    # Sample output
    # [enqueue] Joy, length 0 -> 1
    # [enqueue] Matt, length 1 -> 2
    # [enqueue] Pavel, length 2 -> 3
    # [enqueue] Samir, length 3 -> 4
    # [dequeue] Joy length 4 -> 3, first Joy -> Matt
    # [dequeue] Matt length 3 -> 2, first Matt -> Pavel
    # [dequeue] Pavel length 2 -> 1, first Pavel -> Samir
    # [dequeue] Samir length 1 -> 0, first Samir -> None


if __name__ == "__main__":
    main()
