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
import copy
class graph_node:
    def __init__(self, name):
        self.name = name
        self.paths = []
        self.VISITED = False



def create_nodes(nodes:str):
    letters = dict() # to keep track of num of times a letter appears, then use count to name node appropriately

    labeled_nodes = dict()
    labels = []
    for node in nodes:
        if node not in letters:
            letters[node] = 0
        else:
            letters[node] += 1
        # labeled_nodes.append("{}{}".format(node,letters[node]))  # nodes are in form A0, B0, A1, C0, A2
        gn = graph_node(name=node)
        labeled_nodes["{}{}".format(node, letters[node])] = gn
        labels.append("{}{}".format(node, letters[node]))
    return labeled_nodes, labels


def create_adj_matrix(labeled_nodes, labels, edge_list):
    adj_matrix = {}

    for start, end in edge_list:
        labeled_nodes[labels[start]].paths.append(labels[end])

        if labels[start] not in adj_matrix:
            adj_matrix[labels[start]] = []

        adj_matrix[labels[start]].append(labels[end])

    return labeled_nodes, adj_matrix



def max_path(labeled_nodes, adj_mat:dict):

    # helper returns the most frequent node in the path
    def helper(start_node, next_nodes, frequency_dict, labeled_nodes):
        if labeled_nodes[start_node].VISITED is False:
            labeled_nodes[start_node].VISITED = True
        else:
            return None  # found infinite loop


        temp_dict = {}

        if labeled_nodes[start_node].name in frequency_dict:
            frequency_dict[labeled_nodes[start_node].name] += 1
        else:
            temp_dict[labeled_nodes[start_node].name]=1

        if start_node not in adj_mat:
            combined_dict = dict(**temp_dict,**frequency_dict)
            return max(combined_dict.values())

        max_frequency = 0
        for node in next_nodes:
            nn = [] if node not in adj_mat else adj_mat[node]
            frequency = helper(node, nn, dict(**temp_dict,**frequency_dict), labeled_nodes)
            if frequency is None:
                return None
            max_frequency = max(max_frequency, frequency)

        return max_frequency

    max_path_len = 0
    for node, paths in adj_mat.items():
        path_len = helper(start_node=node, next_nodes=paths, frequency_dict={}, labeled_nodes=copy.deepcopy(labeled_nodes))

        if path_len is None:
            return None

        max_path_len = max(max_path_len, path_len)

    return max_path_len


def find_longest_path(nodes, edge_list):
    # create the nodes. Note each capital letter is a separate node even if has same identifier
    #   eg.'AA'-> node_A, node_A1
    labeled_nodes, labels = create_nodes(nodes)

    # create adjacency matrix for the directed graph
    labeled_nodes, adj_mat = create_adj_matrix(labeled_nodes, labels, edge_list)

    return max_path(labeled_nodes, adj_mat)

if __name__ == '__main__':
    print(find_longest_path('ABACA', edge_list=[(0, 1), (0, 2), (2, 3), (3, 4)]))
    print(find_longest_path('A', edge_list=[(0, 0)]))

