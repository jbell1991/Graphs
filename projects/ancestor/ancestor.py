from graph import Graph

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # instantiate graph class
    graph = Graph()
    # empty path list
    paths = []
    # build graph
    for child, parent in ancestors:
        # add child vertices to the graph
        if child not in graph.vertices:
            graph.add_vertex(child)
        # add parent vertices to the graph
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        # add edges to the graph to the graph
        graph.add_edge(child, parent)

    # search the graph using depth first search
    for vertex in graph.vertices:
        path = graph.dfs(vertex, starting_node)
        if path:
            paths.append(path)
    
    # if length of path is 1 the vertex has no ancestor in the graph
    if len(paths) == 1:
        return -1
    else:
        first_path = paths[0]
        for path in paths:
            if len(path) > len(first_path):
                first_path = path
        return first_path[0]


earliest_ancestor(test_ancestors, 1)
earliest_ancestor(test_ancestors, 2)
# earliest_ancestor(test_ancestors, 3)
# earliest_ancestor(test_ancestors, 4)
# earliest_ancestor(test_ancestors, 5)
# earliest_ancestor(test_ancestors, 6)
# earliest_ancestor(test_ancestors, 7)
# earliest_ancestor(test_ancestors, 8)
# earliest_ancestor(test_ancestors, 9)
# earliest_ancestor(test_ancestors, 10)
# earliest_ancestor(test_ancestors, 11)
