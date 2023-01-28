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


class QueueBuiltWithLinkedList:
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
        # Unset _last so that we don't accidentally maintain a reference to it
        # after we remove the last item from the queue.
        elif self._first == self._last:
            self._last = None
        old_first = self._first
        new_first = self._first.next
        logging.debug(
            f"[dequeue] {old_first} length {self._length} -> {self._length - 1}, "
            f"first {old_first} -> {new_first}"
        )
        self._first = new_first
        self._length -= 1
        return old_first.value


class QueueBuiltWithStacks:
    """
    An implementation of a queue using stacks.

    The idea here is to keep two stacks. One is for pushing items, and one is for popping items.
    But before we do any push/pop operation, we move all the items to that stack so that the
    order of elements is maintained.

    You can picture two stacks whose "bottoms" face each other.

                    stack1   stack2
      push here >>   -----| |-----  >> pop from here

    Let's "enqueue" 2 new items, "x" then "y":

                    stack1   stack2
                     ---yx| |-----

    Now let's "dequeue" an item. "x" should come first because this is a FIFO queue.
    To achieve this, we need to pop all the items from stack1 and move them to stack2.
    Imagine the left end of stack1 and right end of stack2 are connected by a slinky.

                    stack1   stack2
                     -----| |yx---

    Now we can pop from stack2 to get "x"

                    stack1   stack2
                     -----| |y----   >> "x" popped from stack

    To push new items, we just reverse the process.
    """

    def __init__(self) -> None:
        self._front = []
        self._back = []

    @property
    def empty(self) -> bool:
        sum_len = len(self._front) + len(self._back)
        return sum_len == 0

    def peek(self) -> Any:
        if self.empty:
            return None
        elif len(self._front) > 0:
            return self._front[-1]
        else:
            return self._back[0]

    def enqueue(self, value: Any) -> None:
        """
        To maintain order in the queue, move all the items from front to back stack,
        then push the new item to the back stack.
        """
        for _ in range(len(self._front)):
            self._back.append(self._front.pop())
        self._back.append(value)

    def dequeue(self) -> Any:
        for _ in range(len(self._back)):
            self._front.append(self._back.pop())
        return self._front.pop()


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

    queue1 = QueueBuiltWithLinkedList()
    queue2 = QueueBuiltWithStacks()
    for queue in (queue1, queue2):
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


if __name__ == "__main__":
    main()
