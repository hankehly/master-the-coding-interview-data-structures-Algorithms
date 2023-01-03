import logging
import os
from typing import Any

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node = None
        # only used for doubly linked lists
        self.prev: Node = None


class DoublyLinkedList:
    """
    An implementation of a *doubly* linked list.
    To make this a singly linked list, just remove the lines with "prev"
    """

    def __init__(self, value: Any) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value: Any) -> None:
        """
        self.tail is a reference to the last element of self.head, so they're
        referencing the same object in memory. Therefore, an update to self.tail.next
        is reflected in self.head. This means we don't need to use a while loop to get
        the last element of self.head.
        To make this a doubly linked list, we tell the new node its prev is self.tail.
        Time complexity: O(1)
        """
        new = Node(value)
        new.prev = self.tail
        self.tail.next = new
        self.tail = new
        self.length += 1

    def prepend(self, value: Any) -> None:
        """
        Same strategy as append.
        To make this a doubly linked list, we tell the previous head its prev is the new node.
        Time complexity: O(1)
        """
        new = Node(value)
        new.next = self.head
        self.head.prev = new
        self.head = new
        self.length += 1

    def insert(self, index: int, value: Any) -> None:
        """
        Assuming we have the following list:

          index: 0      1      2      3
          value: a <--> b <--> c <--> d

        To insert "foo" at index 2, we would create a new node
        and link it to the nodes immediately before and on the index.
        In other words, you need a reference to the node at 'index' and
        and the node immediately before it.

        To make it a double linked list, we set the prev of the new node and
        the node after it.

        Time complexity: O(1) if first/last item in chain.
                         O(n) if somewhere in the middle.
        """
        if index <= 0:
            self.prepend(value)
        elif index >= self.length - 1:
            self.append(value)
        else:
            pre = self.traverse_to_index(index - 1)
            new = Node(value)
            # link new node and node after it
            new.next = pre.next
            pre.next.prev = new
            # link new node and node before it
            new.prev = pre
            pre.next = new
            self.length += 1

    def remove(self, index):
        """
        Assuming we have the following list:

          index: 0     1     2     3
          value: a --- b --- c --- d

        To remove the head, all we need to do is set self.head = self.head.next.

        To remove the tail, we need to get a reference to the node before it,
        then set it's "next" value to None.

        To remove a node from the middle, we need a reference to the nodes before & after
        it, then we set node_before.next = node_after and let the garbage collector clean
        up the node at index.

        Time complexity: O(1) if index == 0, otherwise O(n)
        """
        index_safe = min(max(index, 0), self.length - 1)
        is_head = index_safe == 0
        is_tail = index_safe == self.length - 1
        logging.debug(
            f"Removing index={index}, index_safe={index_safe}, length={self.length}, "
            f"is_head={is_head}, is_tail={is_tail}"
        )
        logging.debug(f"Before removal: {self}")
        if is_head:
            logging.debug(f"Removing head node (value {self.head.value})")
            self.head.next.prev = None
            self.head = self.head.next
        else:
            pre = self.traverse_to_index(index_safe - 1)
            if is_tail:
                logging.debug(f"Removing tail node (value {pre.next.value})")
                pre.next = None
            else:
                aft = pre.next.next
                aft.prev = pre
                pre.next = aft
        self.length -= 1
        logging.debug(f"After removal: {self}")

    def traverse_to_index(self, index: int) -> Node:
        """
        Returns the node at index.
        To optimize the search, we start iterating from the side (ie head/tail) closest to the index.
        Time complexity: O(n) (technically O(n/2))
        """
        mid_point = self.length // 2
        near_head = index <= self.length - mid_point
        if near_head:
            # iterate forwards using the node.next reference
            c = self.head
            for _ in range(index):
                c = c.next
        else:
            # iterate backwards using the node.prev reference
            c = self.tail
            for _ in range(self.length - 1, index, -1):
                c = c.prev
        return c

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        """
        Builds a string in the format: (node.value) <--> (node.value) <--> ...
        Arrows show prev/next relationship (ie. if relationship doesn't exist, no arrow)
        """
        cursor = self.head
        s = str(cursor.value)
        while cursor.next:
            if cursor.next.prev == cursor:
                s += " <-"
            s += "-> "
            s += str(cursor.next.value)
            cursor = cursor.next
        return s


def main():
    # fmt: off
    my_list = DoublyLinkedList(10) # 10
    my_list.append(2)              # 10 <--> 2
    my_list.append(3)              # 10 <--> 2  <--> 3
    my_list.append(40)             # 10 <--> 2  <--> 3 <--> 40
    my_list.prepend(13)            # 13 <--> 10 <--> 2 <--> 3 <--> 40
    my_list.prepend(99)            # 99 <--> 13 <--> 10 <--> 2 <--> 3 <--> 40
    my_list.insert(2, "hello")     # 99 <--> 13 <--> hello <--> 10 <--> 2 <--> 3 <--> 40
    my_list.insert(5, "world")     # 99 <--> 13 <--> hello <--> 10 <--> 2 <--> world <--> 3 <--> 40
    my_list.remove(0)              # 13 <--> hello <--> 10 <--> 2 <--> world <--> 3 <--> 40
    my_list.remove(200)            # 13 <--> hello <--> 10 <--> 2 <--> world <--> 3
    my_list.remove(2)              # 13 <--> hello <--> 2 <--> world <--> 3
    # fmt: on
    assert str(my_list) == "13 <--> hello <--> 2 <--> world <--> 3"
    assert len(my_list) == 5
    print(my_list)


if __name__ == "__main__":
    main()
