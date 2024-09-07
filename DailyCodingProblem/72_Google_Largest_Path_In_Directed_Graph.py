"""
This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter.
We define a path's value as the number of most frequently-occurring letter along that path.
For example, if a path in the graph goes through "ABACA", the value of the path is 3,
since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.
"""
UNVISITED = 0
VISITING = 1
VISITED = 2

class graph_node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.STATE = UNVISITED  # Possible states UNVISITED, VISITING, VISITED

    def __repr__(self):
        return "(name:{}, neighbours:{})".format(self.name, self.neighbours)


def create_graph(nodes:str, edge_list):
    labeled_nodes = dict()  # save in format 1: graphs_node(name='A')
    for i in range(len(nodes)):
        gn = graph_node(name=nodes[i])
        labeled_nodes[i] = gn

    for start, end in edge_list:  # add all the neighbours to the nodes
        labeled_nodes[start].neighbours.append(end)
    return labeled_nodes


max_freq_memo = {}  # stores maximum frequency letter in path computed from every node


def dfs(start_node, labeled_nodes, frequency_dict=None):  # here since dict is mutable will be shared across instances
    if frequency_dict is None:
        frequency_dict = dict()
    if labeled_nodes[start_node].STATE == VISITED:
        return False
    elif labeled_nodes[start_node].STATE == VISITING:
        return -1 # found a loop

    labeled_nodes[start_node].STATE = VISITING

    # if has neighbours
    if len(labeled_nodes[start_node].neighbours) > 0:
        for neighbour in labeled_nodes[start_node].neighbours:
            frequency_dict = dfs(start_node=neighbour, labeled_nodes=labeled_nodes, frequency_dict={})
            if frequency_dict == -1:
                return -1
            if labeled_nodes[start_node].name not in frequency_dict:
                frequency_dict[labeled_nodes[start_node].name] = 0

            frequency_dict[labeled_nodes[start_node].name] += 1
            if start_node not in max_freq_memo:
                max_freq_memo[start_node] = 0
            max_freq_memo[start_node] = max(max_freq_memo[start_node], max(frequency_dict.values()))

        return frequency_dict

    # executes when no neighbours does not have neighbours
    if labeled_nodes[start_node].name not in frequency_dict:
        frequency_dict[labeled_nodes[start_node].name] = 0

    frequency_dict[labeled_nodes[start_node].name] += 1
    max_freq_memo[start_node] = max(frequency_dict.values())


    labeled_nodes[start_node].STATE = VISITED

    return frequency_dict




def find_longest_path(nodes:str, edge_list:list):
    global max_freq_memo
    max_freq_memo = {}  # rest if filled
    labeled_nodes = create_graph(nodes, edge_list)


    for node_iter in range(len(nodes)):
        if node_iter not in max_freq_memo:
            # perform depth first search
            if dfs(start_node=node_iter, labeled_nodes=labeled_nodes) == -1: # if found a loop
                return None

    return max(max_freq_memo.values())


if __name__ == '__main__':
    assert(find_longest_path('ABACA', edge_list=[(0, 1), (0, 2), (2, 3), (3, 4)])==3)
    assert not (find_longest_path('A', edge_list=[(0, 0)]))
    assert (find_longest_path('ABACADAAA', edge_list=[(0, 1), (1, 5), (5, 6), (6, 7), (7, 8), (0, 2), (2, 3), (3, 4)])==4)
    assert not (find_longest_path('ABC', edge_list=[(0, 1), (1, 2), (2, 1)]))
