import collections
import logging
import os
from typing import Any, List

from section_10_trees.main import BinarySearchTree

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


def linear_search(arr: List[Any], x: Any) -> int:
    """
    A linear search for x in arr.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i


def binary_search(arr: List[int], low: int, high: int, x: int) -> int:
    """
    Instead of recursively calling binary_search on the splitted array (which
    messes up the indices) keep track of where the subset starts and ends.

    The indices get confusing..

    arr: List[int]
        the original array
    low: int
        the index of the first element in the subset
    high: int
        the index of the last element in the subset
    x: int
        the value we are looking for
    """
    if high >= low:
        mid = (low + high) // 2
        logging.debug(
            f"x: {x}, arr[mid]: {arr[mid]}, arr: {arr}, subset: {arr[low:high+1]}, left: {arr[low:mid]}, right: {arr[mid+1:high+1]}, mid: {mid} ({low} + {high} // 2)"
        )
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            # Search the left subset (arr[low:mid])
            # Remember, the 'high' parameter is the last element of the subset we want to include in our search.
            # Setting high=mid-1 here means our next subset will be arr[low:mid], which does not include the current 'mid' value.
            return binary_search(arr, low, mid - 1, x)
        else:
            # Search the right subset.
            return binary_search(arr, mid + 1, high, x)
    return -1


class BreadthFirstSearch:
    def __init__(self, tree: BinarySearchTree):
        self._tree = tree

    def breadth_first_search(self, x):
        """
        Start from the top of the tree, and search top-down left-right order.
        """
        logger = logging.getLogger("breadth_first_search")
        logger.debug(f"Looking for {x}")
        # 1. Create a queue and add the root node to it.
        node = self._tree._root
        queue = collections.deque()
        queue.append(node)
        # 2. Continue until there are no more items left.
        # (We're gonna keep adding items in the body of the while loop)
        while len(queue):
            node = queue.popleft()
            logger.debug(f"dequeue {node.value}")
            logger.debug(f"{node.value} == {x} ({node.value == x})")
            # 3. If the current node is the one you're looking for, great.
            if node.value == x:
                return node
            # 4. Otherwise, add the node's children to the queue (if they exist)
            if node.left:
                logger.debug(f"enqueue {node.left}")
                queue.append(node.left)
            if node.right:
                logger.debug(f"enqueue {node.right}")
                queue.append(node.right)
        logger.debug(f"{x} is not in this tree")
        return None

    def breadth_first_search_recursive(self, queue: collections.deque, x):
        """
        A recursive version of breadth_first_search.
        To keep the state of the queue, we pass it from outside.
        """
        logger = logging.getLogger("breadth_first_search_recursive")
        logger.debug(f"Looking for {x}")
        if len(queue):
            node = queue.popleft()
            logger.debug(f"dequeue {node.value}")
            logger.debug(f"{node.value} == {x} ({node.value == x})")
            if node.value == x:
                return node
            if node.left:
                logger.debug(f"enqueue {node.left}")
                queue.append(node.left)
            if node.right:
                logger.debug(f"enqueue {node.right}")
                queue.append(node.right)
            return self.breadth_first_search_recursive(queue, x)
        logger.debug(f"{x} is not in this tree")
        return None


if __name__ == "__main__":
    names = ["Bob", "George", "Sally"]
    assert linear_search(names, "George") == names.index("George") == 1

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(arr, 0, len(arr) - 1, 1) == 0
    assert binary_search(arr, 0, len(arr) - 1, 3) == 2
    assert binary_search(arr, 0, len(arr) - 1, 8) == 7
    assert binary_search(arr, 0, len(arr) - 1, 30) == -1

    # BST
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
    bfs = BreadthFirstSearch(bst)

    queue1 = collections.deque([bst._root])
    assert (
        bfs.breadth_first_search(15).value
        == bfs.breadth_first_search_recursive(queue1, 15).value
        == 15
    )
    queue2 = collections.deque([bst._root])
    assert (
        bfs.breadth_first_search(152)
        is bfs.breadth_first_search_recursive(queue2, 152)
        is None
    )
