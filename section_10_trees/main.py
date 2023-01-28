import logging
import os
from typing import Any

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


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
        """
        Increasing values go to the right, decreasing values go to the left.
        """
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

    def find_max(self, node: Node) -> Node:
        curr = node
        while curr.right:
            curr = curr.right
        return curr

    def successor(self, node: Node):
        """
        The "successor" of a given node is "the node with the smallest number greater than itself."

        Here's how to look for it:
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


class BinaryMaxHeap:
    """
    A naive implementation of a binary max heap.
    https://visualgo.net/en/heap?slide=5

    https://visualgo.net/en/heap/print
    https://en.wikipedia.org/wiki/Binary_heap

    Notes
    -----
    Does not handle duplicates.
    Logs the whole array if LOGLEVEL=debug.
    Indices are from 1+
    """

    def __init__(self):
        self._data = []

    def __repr__(self) -> str:
        return str(self._data)

    @property
    def empty(self) -> bool:
        return len(self._data) == 0

    def _iparent(self, i: int) -> int:
        """
        Returns the INDEX of the parent of item at index `i`
        To get the parent index of a node at index N, we take N // 2 (integer division)
        """
        assert i > 0
        return i // 2

    def _ileft(self, i: int) -> int:
        """
        Note: Be careful with i=0
        """
        assert i > 0
        return i * 2

    def _iright(self, i: int) -> int:
        """
        Note: Be careful with i=0
        """
        assert i > 0
        return i * 2 + 1

    def insert(self, v: int):
        """
        To insert into a binary heap, we first add the new element at the last position of the array,
        then "shift up" until the tree maintains the Max Heap property (the parent of each vertex is
        always bigger than the vertex itself - except for the root element)

        We manage the data as an array. The index corresponds to the position of the element.
          [6, 4, 3, 2, 1]
        Would look like this..

                  6        < position 1
                 / \
                4   3      < positions 2, 3
               / \
              2   1        < positions 4, 5

        We always add elements from LEFT to RIGHT.

        Let's say we want to insert 9 in this heap:
          [6, 4, 3, 2, 1]

        Here are the steps.
        1. Add to last place
          [6, 4, 3, 2, 1, 9]
        2. Compare with parent, swap if parent < value
           Parent is at index(9) // 2, so 5//2=2, which corresponds to value 3.
           3 < 9, so swap them.
          [6, 4, 9, 2, 1, 3]
        3. Continue..
           index(9) // 2, so 2 // 2, so 1
           4 < 9, so swap them.
          [6, 9, 4, 2, 1, 3]
        4. Continue..
           index(9) // 2, so 1 // 2, so 0
           6 < 9, so swap them.
          [9, 6, 4, 2, 1, 3]

          Done!
        """
        logging.debug(f"insert({v})")
        self._data.append(v)
        logging.debug(f"after insert: {self._data}")
        if len(self._data) == 1:
            return
        # You will always add values to the end of the array, so the added value will always be a leaf.
        # This means you only have to worry about checking ABOVE it.
        self._shift_up(len(self._data))

    def _shift_up(self, i: int):
        """
        See `insert` docstring for an example of how this works.
        """
        logging.debug(f"shift_up({i})")
        curr_pos = i
        parent_pos = self._iparent(curr_pos)
        while parent_pos and self._data[parent_pos - 1] < self._data[curr_pos - 1]:
            logging.debug(f"before shift_up: {self._data}")
            logging.debug(f"swap parent(i={parent_pos}) for current(i={curr_pos})")
            # fmt: off
            self._data[parent_pos-1], self._data[curr_pos-1] = self._data[curr_pos-1], self._data[parent_pos-1]
            logging.debug(f"after shift_up: {self._data}")
            curr_pos = parent_pos
            parent_pos = self._iparent(curr_pos)
            logging.debug(f"curr_pos={curr_pos}, parent_pos={parent_pos}")
            # fmt: on

    def _shift_down(self, i: int):
        """
        While there is a child greater than the current vertex, swap.
        """
        logging.debug(f"shift_down({i})")
        curr_i = i
        child_i = self._greater_child_position(curr_i)
        while child_i:
            logging.debug(f"before shift_down: {self._data}")
            logging.debug(
                f"shift_down: swap child(i={child_i},v={self._data[child_i-1]}) "
                f"for current(i={curr_i},v={self._data[curr_i-1]}) (1-indexed)"
            )
            # fmt: off
            self._data[curr_i - 1], self._data[child_i - 1] = self._data[child_i - 1], self._data[curr_i - 1]
            # fmt: on
            logging.debug(f"after shift_down: {self._data}")
            curr_i = child_i
            child_i = self._greater_child_position(curr_i)

    def _greater_child_position(self, i: int) -> int:
        assert i > 0
        vself = self._data[i - 1]
        a_len = len(self._data)
        ileft = self._ileft(i)
        iright = self._iright(i)
        if iright <= a_len:
            # has both
            vleft = self._data[ileft - 1]
            vright = self._data[iright - 1]
            if vleft > vright and vleft > vself:
                return ileft
            elif vright > vleft and vright > vself:
                return iright
        elif ileft <= a_len:
            # has left only
            vleft = self._data[ileft - 1]
            if vleft > vself:
                return ileft
        # has no children greater than itself
        return None

    def extract_max(self):
        """
        The max element will always be self._data[0] (unless root is NULL)

        When we remove the max element, we have to replace it with something.
        That something is the last (leaf) element. We do this to maintain a compact (no spaces)
        structure. However, moving a leaf to the first position will probably violate
        the Max Heap property, so we need to then "shift down" the first element by
        comparing it to its children and swapping until we meet this requirement.
        """
        logging.debug(f"extract_max()")
        if self.empty:
            return None
        elif len(self._data) == 1:
            return self._data.pop()
        else:
            # Make the initial swap (root node for last element)
            logging.debug(f"starting point: {self._data}")
            self._data[0], self._data[-1] = self._data[-1], self._data[0]
            logging.debug(f"after initial swap: {self._data}")
            # Get the last value (which we know is the max) for returning later
            max_value = self._data.pop()
            logging.debug(f"after pop: {self._data}")
            # Shift the element at index 0 downward.
            # Use 1-based indices to prevent zero-multiplication during child search.
            self._shift_down(1)
            return max_value

    def find_max(self):
        """
        O(1)
        """
        if self.empty:
            return None
        return self._data[0]


class PriorityQueue:
    """
    You can see that a priority queue can be implemented as just a Binary Heap.

    Here is python's implementation.
    https://docs.python.org/3/library/heapq.html

    It also has some interesting suggestions for how to implement a Priority Queue.
    https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes

    Example:
    We store a heap as an array.
    >>> import heapq
    >>> heap = []

    heapq only supports Min heap, so to make it a Max heap, multiply
    values by -1 before adding. This will keep the numbers in Max order (assuming
    you multiply them again by -1 after extracting the head)
    >>> heapq.heappush(heap, 5*-1)
    >>> heapq.heappush(heap, 10*-1)
    >>> heap
    [-10, -5]
    >>> heapq.heappush(heap, 15*-1)
    >>> heapq.heappush(heap, 20*-1)
    >>> heap
    [-20, -15, -10, -5]
    >>> heapq.heappush(heap, 3*-1)
    >>> heap
    [-20, -15, -10, -5, -3]
    >>> heapq.heappop(heap) * -1
    20

    Here's an implementation example using heapq.
    https://github.com/stevenhalim/cpbook-code/blob/master/ch2/nonlineards/priority_queue.py
    """

    def __init__(self):
        self._binary_heap = BinaryMaxHeap()

    def enqueue(self, v: int):
        self._binary_heap.insert(v)

    def dequeue(self, v: int):
        return self._binary_heap.extract_max()


def test_binary_search_tree():
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

    # Check that find_min returns the minimum value at a specific subtree
    assert bst.find_min(bst.lookup(9)).value == 1
    assert bst.find_min(bst.lookup(20)).value == 15

    # Check that successor returns the smallest value greater than the target
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


def test_binary_heap():
    heap = BinaryMaxHeap()
    heap.insert(1)
    heap.insert(2)
    assert heap._data == [2, 1]
    heap.insert(4)
    assert heap.find_max() == 4
    assert heap._data == [4, 1, 2]
    heap.insert(6)
    assert heap.find_max() == 6
    assert heap._data == [6, 4, 2, 1]
    heap.insert(3)
    assert heap.find_max() == 6
    assert heap._data == [6, 4, 2, 1, 3]
    heap.insert(9)
    assert heap.find_max() == 9
    assert heap._data == [9, 4, 6, 1, 3, 2]
    # extract_max operation should return elements in max->min order
    assert heap.extract_max() == 9
    assert heap.extract_max() == 6
    assert heap.extract_max() == 4
    assert heap.extract_max() == 3
    assert heap.extract_max() == 2
    assert heap.extract_max() == 1
    assert heap.extract_max() is None


def main():
    test_binary_search_tree()
    test_binary_heap()


if __name__ == "__main__":
    main()
