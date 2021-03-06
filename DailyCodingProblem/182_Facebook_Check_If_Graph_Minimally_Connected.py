"""
This problem was asked by Facebook.

A graph is minimally-connected if it is connected and there is no edge that can be removed while
still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.
You can choose to represent the graph as either an adjacency matrix or adjacency list.
"""

# idea : whenever a loop of paths forms the graph is not minimally connected.
# this is depth first search
def is_minimally_connected(adj_list:dict):

    def helper(curr_node, next_paths, visited_paths):
        state=True
        for path in next_paths:
            if len(visited_paths) > 0 and path == visited_paths[-1]:
                continue  # coming from node visited_paths[-1]
            if path in visited_paths:
                return False  # created a loop, so not minimally connected

            state = state and helper(path, adj_list[path], visited_paths + [curr_node])

        return state  # all nodes checked, so minimally connected

    keys = list(adj_list.keys())
    return helper(keys[0], adj_list[keys[0]], [])


# simpler approach see that in a minimally connected tree there can only be
# n - 1 edges. Eg:
# if number of nodes n = 1 the e = 0
# if number of nodes n = 2 the e = 1
# if number of nodes n = 3 the e = 2

def is_minimally_connected_redux(adj_list:dict):
    number_of_nodes = len(adj_list)
    number_edges = 0
    visited_nodes = set()
    for node, paths in adj_list.items():
        visited_nodes.add(node)
        for next_nodes in paths:
            if next_nodes not in visited_nodes:
                number_edges += 1


    return number_of_nodes - 1 == number_edges


if __name__ == '__main__':

    """
                 a 
                / \
               b   c
                \ / \
                 d - e 
    """

    graph_1 = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd', 'e'],
        'd': ['b', 'c', 'e'],
        'e': ['c', 'd']
    }

    print(is_minimally_connected(graph_1))
    print(is_minimally_connected_redux(graph_1))
    """
                a
               / \
              b   c
                 / \
                d   e
    """

    graph_1 = {
        'a': ['b', 'c'],
        'b': ['a'],
        'c': ['a', 'd', 'e'],
        'd': ['c'],
        'e': ['c']
    }

    print(is_minimally_connected(graph_1))
    print(is_minimally_connected_redux(graph_1))
    """
                    a
                   / \
                  b   c
                     / \
                    d - e
    """

    graph_1 = {
        'a': ['b', 'c'],
        'b': ['a'],
        'c': ['a', 'd', 'e'],
        'd': ['c', 'e'],
        'e': ['c', 'd']
    }

    print(is_minimally_connected(graph_1))
    print(is_minimally_connected_redux(graph_1))
