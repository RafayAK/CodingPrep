"""
This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain,
and a number of steps num_steps. Run the Markov chain starting from start for num_steps
and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""

import random


def parse_markov_chain(states):
    state_transition_dict = {}

    for state in states:
        start, end, prob = state
        if start not in state_transition_dict:
            # the first list contains the possible path not a node and the second
            # list contains the relative weight to transition to that node
            state_transition_dict[start] = ([], [])
            state_transition_dict[start][0].append(end)
            state_transition_dict[start][1].append(prob)
        else:
            # # convert transition probabilities to cumulative weights
            # # i.e [1,2,3,4,5] --> [1 3 6 10 15]
            # #     [0.5, 0.25, 0.25] --> [0.5, 0.75, 1.00]
            # # this saves some time when running random.choices
            state_transition_dict[start][0].append(end)
            state_transition_dict[start][1].append(state_transition_dict[start][1][-1] + prob)

    return state_transition_dict


def run_markov_model(states, runs=5000):
    state_transition_dict = parse_markov_chain(states)
    nodes = list(state_transition_dict.keys())
    result = {node : 0 for node in nodes}
    print(result)
    starting_node = nodes[0]
    print(starting_node)
    nodes, weights = state_transition_dict[starting_node]
    for _ in range(5000):
        res = random.choices(nodes, cum_weights=weights)[0]
        result[res] += 1
        nodes, weights = state_transition_dict[res]

    return result

if __name__ == '__main__':

    print(run_markov_model([
      ('a', 'a', 0.9),
      ('a', 'b', 0.075),
      ('a', 'c', 0.025),
      ('b', 'a', 0.15),
      ('b', 'b', 0.8),
      ('b', 'c', 0.05),
      ('c', 'a', 0.25),
      ('c', 'b', 0.25),
      ('c', 'c', 0.5)
    ]))

