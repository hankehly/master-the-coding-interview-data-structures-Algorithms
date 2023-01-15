import json
from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
    def __init__(self) -> None:
        self._root = None

    def insert(self, value: Any) -> None:
        new_node = Node(value)
        if self._root is None:
            self._root = new_node
        else:
            node = self._root
            while True:
                if value > node.value:
                    if node.right is None:
                        node.right = new_node
                        break
                    else:
                        node = node.right
                elif value < node.value:
                    if node.left is None:
                        node.left = new_node
                        break
                    else:
                        node = node.left
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


if __name__ == "__main__":
    main()
