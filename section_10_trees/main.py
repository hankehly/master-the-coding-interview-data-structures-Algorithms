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
        return len(list(filter(None, (self.left, self.right))))

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)

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
                     67  95
                    /
                   65

        The successor of 64 is 65.
        The successor of 95 is 96.
        The successor of 67 is 71.
        etc..
        """
        if node.right:
            return self.find_min(node.right)
        curr = node
        # Keep traversing upwards until we make a 'right turn'
        while curr.parent and curr == curr.parent.right:
            curr = curr.parent
        # At this point, the parent either doesn't exist, or we made a 'right turn'
        if curr.parent is None:
            return None  # there is no successor
        if curr == curr.parent.left:
            return curr.parent

    def remove(self, value: Any):
        """
        This was tough! I had to use visualgo to understand the steps.
        https://visualgo.net/en/bst

        There are 3 cases to consider:
         1. Leaf node
         2. Single child
         3. 2 children

        In case (1) we just delete the node.
        In case (2) we "bypass" the node by connecting the parent/children together.
        In case (3) we have to find the appropriate "successor" (which is defined above) then replace the node with it.

        The hardest part was the successor replacement. To figure it out, I visualized the steps in draw.io.
        See the README for details.
        """
        node = self.lookup(value)
        if node is None:
            return
        # If this is a leaf node, just delete it
        elif node.nchildren == 0:
            if node == self._root:
                self._root = None
            else:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
        # If node has 1 child, bypass node and set its child as the child of node.parent
        elif node.nchildren == 1:
            succ = node.right if node.left is None else node.left
            if node.value < node.parent.value:
                node.parent.left = succ
            else:
                node.parent.right = succ
        # Otherwise, replace node with its successor
        else:
            succ = self.successor(node)

            # Update the target's parent to point to 'successor' as its child
            # If no parent exists, this is the root node, so set it to NULL and return, we're done!
            if node.parent:
                if node.value < node.parent.value:
                    node.parent.left = succ
                else:
                    node.parent.right = succ
            else:
                self._root = None
                return

            # Update the successor's parent to point to NULL as it's child.
            # (ie disconnect the successor from its original parent)
            if succ.value < succ.parent.value:
                succ.parent.left = None
            else:
                succ.parent.right = None

            # Set successor's parent to the removal target node's parent
            succ.parent = node.parent

            # Set the removal target node's parent to NULL
            # (ie. disconnect target node from parent)
            node.parent = None

            # Set the successor's children to the removal target node's children
            succ.left = node.left
            succ.right = node.right
            # import pdb; pdb.set_trace()

            # Set removal target node children's parent to successor
            if node.left:
                node.left.parent = succ
            if node.right:
                node.right.parent = succ

            # Set removal node target children to NULL
            # (maybe unnecessary, but I want to isolate target node completely)
            node.left = None
            node.right = None


def traverse(node: Node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left)
    tree["right"] = None if node.right is None else traverse(node.right)
    return tree


def main():
    # Build this tree:
    #      9
    #    /   \
    #   4     20
    #  / \    / \
    # 1   6 15  170
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(20)
    bst.insert(1)
    bst.insert(6)
    bst.insert(15)
    bst.insert(170)

    # Check tree structure
    act = traverse(bst._root)
    exp = {
        "value": 9,
        "left": {
            "value": 4,
            "left": {"value": 1, "left": None, "right": None},
            "right": {"value": 6, "left": None, "right": None},
        },
        "right": {
            "value": 20,
            "left": {"value": 15, "left": None, "right": None},
            "right": {"value": 170, "left": None, "right": None},
        },
    }
    assert act == exp

    # Check that lookup returns the correct nodes
    assert bst.lookup(6).value == 6
    assert bst.lookup(9).value == 9
    assert bst.lookup(15).value == 15
    assert bst.lookup(40) == None
    assert bst.find_min(bst.lookup(9)).value == 1
    assert bst.find_min(bst.lookup(20)).value == 15
    assert bst.successor(bst.lookup(6)).value == 9
    assert bst.successor(bst.lookup(170)) is None

    # Remove some nodes and re-check tree structure
    bst.remove(20)
    bst.remove(1)
    act = traverse(bst._root)
    exp = {
        "value": 9,
        "left": {
            "value": 4,
            "left": None,
            "right": {"value": 6, "left": None, "right": None},
        },
        "right": {
            "value": 170,
            "left": {"value": 15, "left": None, "right": None},
            "right": None,
        },
    }
    assert act == exp


if __name__ == "__main__":
    main()
