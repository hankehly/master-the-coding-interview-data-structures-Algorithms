import logging
import os

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)


class Graph:
    """
    An implementation of a graph using an *adjacent list*.

    We use an object as the internal data structure instead of an array because
    we don't know how many vertices will be added to the adjacent list, and to
    use an array might requires lots of shifting of elements (bad performance).
    An object (hash table) is more performant in this case.
    """

    def __init__(self):
        self._number_of_nodes = 0
        self._adjacent_list = {}

    def add_vertex(self, vertex: int):
        """
        If the vertex already exists, do nothing.
        Otherwise, initialize as a new list.
        """
        if vertex in self._adjacent_list:
            logging.warn(f"Vertex with value {vertex} already exists.")
        else:
            self._adjacent_list[vertex] = []

    def add_edge(self, vertex1: int, vertex2: int):
        if vertex1 in self._adjacent_list and vertex2 in self._adjacent_list:
            self._adjacent_list[vertex1].append(vertex2)
            self._adjacent_list[vertex2].append(vertex1)
        else:
            raise ValueError(f"Vertices {vertex1} and/or {vertex2} missing from graph.")

    def show_connections(self):
        output = ""
        for vertex in self._adjacent_list:
            output += (
                f"{vertex} --> {' '.join(map(str, self._adjacent_list[vertex]))}\n"
            )
        print(output)


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_edge(3, 1)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    graph.add_edge(4, 5)
    graph.add_edge(1, 2)
    graph.add_edge(1, 0)
    graph.add_edge(0, 2)
    graph.add_edge(6, 5)
    graph.show_connections()
    # Answer (order of elements on right-side may be different)
    # 0 --> 1 2
    # 1 --> 3 2 0
    # 2 --> 4 1 0
    # 3 --> 1 4
    # 4 --> 3 2 5
    # 5 --> 4 6
    # 6 --> 5
