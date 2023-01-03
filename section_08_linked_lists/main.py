from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node = None


class LinkedList:
    """
    {
        "value": 1,
        "next": {
            "value": 2,
            "next": {
                "value: 3,
                "next": None
            }
        }
    }
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

        Time complexity: O(1)
        """
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value: Any) -> None:
        """
        Time complexity: O(1)
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index: int, value: Any) -> None:
        """
        Assuming we have the following list:

          index: 0     1     2     3
          value: a --- b --- c --- d

        To insert "foo" at index 2, we would create a new node
        and link it to the nodes immediately before and on the index.
        In other words, you need a reference to the node at 'index' and
        and the node immediately before it.

        Time complexity: O(1) if first/last item in chain.
                         O(n) if somewhere in the middle.
        """
        if index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)
        else:
            # Since all nodes have a reference to the next node
            # we should find the node immediately before the node at index
            node_pre = self.head
            for _ in range(index - 1):
                node_pre = node_pre.next
            new_node = Node(value)
            new_node.next = node_pre.next
            node_pre.next = new_node
            self.length += 1

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        """
        Format:
        x --> y --> z
        """
        n = self.head
        values = [n.value]
        while n.next:
            n = n.next
            values.append(n.value)
        result = " --> ".join(map(str, values))
        return result


def main():
    my_list = LinkedList(10)
    my_list.append(2)
    my_list.append(3)
    my_list.prepend(13)
    my_list.insert(2, "hello")
    assert str(my_list) == "13 --> 10 --> hello --> 2 --> 3"
    print(my_list)


if __name__ == "__main__":
    main()
