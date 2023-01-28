# Section 11: Data Structures: Graphs

A linked list is a type of tree. Trees are a type of graph.
Graphs are good for defining relationships.
Neo4J is a popular graph database.

Term | Meaning
:- | :-
Vertex | Node
Edge | Line connecting 2 vertices. Can store information (unlike trees)
Directed Graph | Traffic flows in specific way (ex. one-way roads)
Undirected Graph | Bi-directional traffic flow (ex. highway)
Weighted Graph | Edges have values (12, -2, etc.), often used for calculating optimal paths
Unweighted Graph | All edges are equal
Cyclic Graph | Can loop around nodes at SOME locations (not required for all), common in weighted graphs
Acyclic Graph | Can't travel back to the starting point, not connected in a loop
DAG | Directed Acyclic Graph

### Edge List

A way of describing a graph as a list of connections. A list of pairs. The index of the pair is irrelevant (as opposed to adjacent lists/matrices).

```py
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]
```

[![](https://mermaid.ink/img/pako:eNpFjjEOwjAMRa9SeW4kWrbMsMECqxercWmkJqmCM6Cqd8c0qvD0_PRt_RWG5BgsvDItU3N7YGx0TsaYvmKveP5jV7E7LLQQOAfyTp-sP4MgEwdGsIqORyqzIGDcNFoWR8JX5yVlsJILt0BF0vMTh2OvmYsnrRTAjjS_1fJ-c69l987bF4SqOXs?type=png)](https://mermaid.live/edit#pako:eNpFjjEOwjAMRa9SeW4kWrbMsMECqxercWmkJqmCM6Cqd8c0qvD0_PRt_RWG5BgsvDItU3N7YGx0TsaYvmKveP5jV7E7LLQQOAfyTp-sP4MgEwdGsIqORyqzIGDcNFoWR8JX5yVlsJILt0BF0vMTh2OvmYsnrRTAjjS_1fJ-c69l987bF4SqOXs)

### Adjacent List

Another way of describing a graph. Uses an array index (or object key) as the value of the vertex, and sets the array (or object) value to the values of the connected vertices.

We could represent the above graph like this.

```py
graph = [
    [2],        # vertex 0 is connected to vertex 2
    [2, 3],     # vertex 1 is connected to vertices 2 and 3
    [0, 1, 3],  # vertex 2 is connected to vertices 0, 1 and 3
    [1, 2]      # vertex 3 is connected to vertices 1 and 2
]
```

If the vertex values are not sequential numbers, it would be more helpful to use an object.

### Adjacent Matrix

Another way of describing graphs, using a matrix of 1s and 0s. Like an adjacent list, the index of the row is the current vertex value. The value at each index is a list of 1s and 0s indicating whether or not the vertex has a relationship with the vertex in that position.

We can represent the graph above like this.

```py
graph = [
    [0, 0, 1, 0], # vertex 0 is connected to vertex 2
    [0, 0, 1, 1], # vertex 1 is connected to vertices 2 and 3
    [1, 1, 0, 1], # vertex 2 is connected to vertices 0, 1 and 3
    [0, 1, 1, 0], # vertex 3 is connected to vertices 1 and 2
]
```

You can also use an object.

```py
graph = {
    0: [0, 0, 1, 0],
    1: [0, 0, 1, 1],
    2: [1, 1, 0, 1],
    3: [0, 1, 1, 0],
}
```
