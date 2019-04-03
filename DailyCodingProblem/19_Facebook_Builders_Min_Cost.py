'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build
the nth house with kth color, return the minimum cost which achieves this goal.
'''


import copy
def min_cost(costs_matrix): # dp problem
    # create a zeros filled list the size of costs_matrix
    # to store costs at each decision
    rows = len(costs_matrix)
    cols = len(costs_matrix[0])
    best_costs = [[0]*cols for _ in range(rows)]

    # best costs for each color for the first house is trivial => same as the provided costs
    best_costs[0] = copy.deepcopy(costs_matrix[0])

    # iterate over rest of the houses => houses[1:]
    for house in range(1, rows):
        for color in range(cols):
            best_costs[house][color] = costs_matrix[house][color] + min(best_costs[house-1][:color] + best_costs[house-1][color+1:])


    return min(best_costs[len(best_costs)-1])

if __name__ == '__main__':
    # costs_mat = [[1,2,5], [1,2,5], [1,2,5]]
    costs_mat = [[0.1,0.7, 0.9], [.1, 10 , 9], [99, 200, 47]]
    print(min_cost(costs_mat))
