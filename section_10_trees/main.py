import json
from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None

    @property
    def nchildren(self) -> int:
        return len(filter(None, (self.left, self.right)))

    def get_only_child(self) -> "Node":
        if self.nchildren != 1:
            raise Exception(f"Node has {self.nchildren}")
        elif self.left:
            return self.left
        else:
            return self.right

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, node: "Node") -> bool:
        return self.value == node.value


class BinarySearchTree:
    def __init__(self) -> None:
        self._root = None

    def insert(self, value: Any) -> None:
        new_node = Node(value)
        if self._root is None:
            self._root = new_node
        else:
            curr = self._root
            while True:
                if value > curr.value:
                    if curr.right is None:
                        curr.right = new_node
                        new_node.parent = curr
                        break
                    else:
                        curr = curr.right
                elif value < curr.value:
                    if curr.left is None:
                        curr.left = new_node
                        new_node.parent = curr
                        break
                    else:
                        curr = curr.left
                else:
                    break  # already exists!

    def lookup(self, value: Any) -> Node:
        if self._root is None:
            return None
        else:
            current = self._root
            while current:
                if value > current.value:
                    current = current.right
                elif value < current.value:
                    current = current.left
                else:
                    return current
            return None

    def find_min(self, node: Node) -> Node:
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def successor(self, node: Node):
        """
        The "successor" of a given node is the node with the smallest number greater than itself.

        1. First, we should look for the smallest number in the right subtree.
        2. If there is no right subtree, the successor must be above the current node.
        To find it, we should look for the parent of the subtree that has `node` on its left side.

        Let's take the following example.

                       96
                      /  \
                    64    99
                   /  \
                 61    71
                      /  \
                     67  105
                    /
                   65

        The successor of 64 is 65.
        The successor of 105 is 96.
        The successor of 67 is 71.
        etc..
        """
        if node.right:
            return self.find_min(node.right)
        else:
            curr = node
            # keep traversing upwards until we make a right turn
            while curr.parent and curr == curr.parent.right:
                curr = curr.parent
            if curr.parent is None:
                return None  # there is no successor
            if curr == curr.parent.left:
                return curr.parent

    def remove(self, value: Any):
        """
        xxx
        """
        if self._root is None:
            return None
        # 1. Find the target node and its predecessor
        curr = self._root
        while curr:
            if value > curr.value:
                curr = curr.right
            elif value < curr.value:
                curr = curr.left
            else:
                break
        # If this is a leaf node, just delete it and delete parent.left
        # or parent.right accordingly
        if curr.nchildren == 0:
            if curr == self._root:
                self._root = None
            else:
                if curr == curr.parent.left:
                    curr.parent.left = None
                else:
                    curr.parent.right = None
        elif curr.nchildren == 1:
            # bypass current and set its child as the child of curr.parent
            child = curr.get_only_child()
            if curr == curr.parent.left:
                curr.parent.left = child
            elif curr == curr.parent.right:
                curr.parent.right = child
        else:

            pass


def traverse(node: Node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left)
    tree["right"] = None if node.right is None else traverse(node.right)
    return tree


def main():
    #     9
    #  4    20
    # 1 6  15 170
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(20)
    bst.insert(1)
    bst.insert(6)
    bst.insert(15)
    bst.insert(170)
    # Check tree structure
    # print(json.dumps(traverse(bst._root)))
    # Check that lookup returns the correct nodes
    assert bst.lookup(6).value == 6
    assert bst.lookup(9).value == 9
    assert bst.lookup(15).value == 15
    assert bst.lookup(40) == None
    assert bst.find_min(bst.lookup(9)).value == 1
    assert bst.find_min(bst.lookup(20)).value == 15
    assert bst.successor(bst.lookup(6)).value == 9
    assert bst.successor(bst.lookup(170)) is None
    # bst.insert(100)
    # bst.insert(180)
    # bst.remove(170)
    # bst.remove(20)
    # print(json.dumps(traverse(bst._root)))


if __name__ == "__main__":
    main()
