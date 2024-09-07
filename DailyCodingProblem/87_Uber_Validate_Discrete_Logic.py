"""
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
"""

opposites = {'N':'S', 'S':'N', 'E':'W', 'W':'E'}

class Node:
    def __init__(self, point):
        self.point = point
        self.neighbours = {
            'N': None,
            'S': None,
            'E': None,
            'W': None
        }

    def check_conflict(self, direction, node):
        if self.neighbours[direction]:
            if self.neighbours[direction].point == node.point:
                print("->>>> {} already exists \"{}\" of {}".format(node.point, direction,
                                                              self.neighbours[opposites[direction]].point))
                return -1
            else:
                return self.neighbours[direction].check_conflict(direction, node)

        return 1

    def add_node_in_direction(self, direction, node):
        for char in direction:
            conflict_status = self.check_conflict(opposites[char], node)

            if conflict_status == -1:
                print("->>>> {} can't be added \"{}\" of {}".format(node.point, direction, self.point))
                return -1

            # if no conflict then check if there is already a node in the 'direction',
            # if node in direction exists check if not its same node we want to add
            # if both conditions pass then go deeper in the 'direction'
            if self.neighbours[char]:
                if self.neighbours[char].point != node.point:
                    self.neighbours[char].add_node_in_direction(direction, node)
            else:
                # found empty spot
                self.neighbours[char] = node
                node.neighbours[opposites[char]] = self



    def __repr__(self):
        string = "{}=[N: {}, S: {}, E: {}, W: {}]".format(self.point,
                                                       self.neighbours['N'].point if self.neighbours['N'] else '-',
                                                       self.neighbours['S'].point if self.neighbours['S'] else '-',
                                                       self.neighbours['E'].point if self.neighbours['E'] else '-',
                                                       self.neighbours['W'].point if self.neighbours['W'] else '-')
        return string



def validate_rules(rules):

    nodes = dict()
    status = 0
    for rule in rules:
        p1, direc, p2 = rule

        if p1 not in nodes:
            # create node_p1
            nodes[p1] = Node(p1)
        if p2 not in nodes:
            nodes[p2] = Node(p2)

        status = nodes[p2].add_node_in_direction(direc, nodes[p1])

        if status == -1:
            print('Conflict!')
            break

    if status != -1:
        print('Success!')




if __name__ == '__main__':

    """     C
            |
            A
            |
          C-B
            |
            C
            |
            A
    
    """

    rules = [
        ['A', 'N', 'B'],
        ['B', 'NE', 'C'],
        ['C', 'N', 'A']
             ]
    validate_rules(rules)


    """
            
            A
            |
            B-A
    """


    rules = [
        ['A', 'NE', 'B'],
        ['A', 'N', 'B'],
    ]
    validate_rules(rules)

    """     
               A
               |
             C-B
               |
               C

    """

    rules = [
        ['A', 'N', 'B'],
        ['B', 'NE', 'C'],
        ['C', 'S', 'A']
    ]
    validate_rules(rules)


    """     
               A
               |
           D-C-B-D 
               |
               C

    """

    rules = [
        ['A', 'N', 'B'],
        ['B', 'NE', 'C'],
        ['C', 'S', 'A'],
        ['D', 'E', 'B'],
        ['D', 'W', 'C']
    ]
    validate_rules(rules)


