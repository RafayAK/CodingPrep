"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.
"""


# creates a 2 object list out of each and adds None to the place where we'll mark the color of the node
def get_nodes(adj_mat):
    return [[i, None] for i in range(len(adj_mat))]


def check_nodes_filled(nodes):
    # check if all nodes are filled
    return all((val[1] for val in nodes))


def check_valid(curr_node, nodes, adj_mat):

    for node,edge in enumerate(adj_mat[curr_node[0]]):
        if edge == 1:
             if nodes[node][1] == curr_node[1]:
                return False

    return True


def add_color(nodes, k):
    # take the first node with None as the second attr
    current_node = None
    for n in nodes:
        if n[1] is None:
            current_node = n
            break

    # check if all nodes are colored
    if current_node is None:
        return nodes

    # try to add color to the node:
    for color in k:

        current_node[1] = color
        if check_valid(current_node, nodes,adjacency_mat):
            # if True
            result = add_color(nodes, k)

            if check_nodes_filled(result):
                return result

        current_node[1] = None

    return nodes


def solve(adj_mat, k):
    result = add_color(get_nodes(adjacency_mat), k)

    return result, check_nodes_filled(result)



if __name__ == '__main__':
    """
    
    (a)---(b) 
     |  \/  
     |  /\  
     | /  \
    (c)---(d) 
    
    """


    adjacency_mat = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    print(solve(adjacency_mat, ['r', 'g', 'b']))

