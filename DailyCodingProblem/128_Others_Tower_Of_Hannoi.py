"""
The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the
bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the
rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
"""

from copy import deepcopy

# Breadth-first search solution
# Very poor performance


class hanoi:
    def __init__(self):
        self.peg_1 = []  # stack 1
        self.peg_2 = []  # stack 2
        self.peg_3 = []  # stack 3
        self.moves = []
        self.num_of_disks = 0

    def add_discs(self, n):
        # add all the discs to peg_1
        self.num_of_disks = n
        for i in range(1, n + 1):
            self.peg_1.append(i)

    def execute_move(self):
        new_game_states = []

        # see if discs from peg_1 can be moved:
        if self.peg_1:
            # pick first disk:
            disk = self.peg_1[0]
            # see if it can be moved to other two pegs
            if len(self.peg_2) ==0 or self.peg_2[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_1.pop(0)  # pick up disk
                new_state.peg_2.insert(0, disk)
                new_state.moves.append('Move {} to 2'.format(disk))
                new_game_states.append(new_state)
            if len(self.peg_3) == 0 or self.peg_3[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_1.pop(0)  # pick up disk
                new_state.moves.append('Move {} to 3'.format(disk))
                new_state.peg_3.insert(0, disk)
                new_game_states.append(new_state)

        # see if discs from peg_2 can be moved:
        if self.peg_2:
            # pick first disk:
            disk = self.peg_2[0]
            # see if it can be moved to other two pegs
            if len(self.peg_1) == 0 or self.peg_1[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_2.pop(0)  # pick up disk
                new_state.peg_1.insert(0, disk)
                new_state.moves.append('Move {} to 1'.format(disk))
                new_game_states.append(new_state)
            if len(self.peg_3) == 0 or self.peg_3[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_2.pop(0)  # pick up disk
                new_state.peg_3.insert(0, disk)
                new_state.moves.append('Move {} to 3'.format(disk))
                new_game_states.append(new_state)

        # see if discs from peg_3 can be moved:
        if self.peg_3:
            # pick first disk:
            disk = self.peg_3[0]
            # see if it can be moved to other two pegs
            if len(self.peg_1) == 0 or self.peg_1[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_3.pop(0)  # pick up disk
                new_state.peg_1.insert(0, disk)
                new_state.moves.append('Move {} to 1'.format(disk))
                new_game_states.append(new_state)
            if len(self.peg_2) == 0 or self.peg_2[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_3.pop(0)  # pick up disk
                new_state.peg_2.insert(0, disk)
                new_state.moves.append('Move {} to 2'.format(disk))
                new_game_states.append(new_state)

        return new_game_states


    def solved(self):
        if len(self.peg_3) == self.num_of_disks:
            return True

    def __repr__(self):
        return "1:{}    , 2: {},    3:{}".format(self.peg_1, self.peg_2, self.peg_3)



def solve_hanoi(game):
    queue = []
    queue.append(game)

    while queue:
        # print(len(queue))
        curr_game_state = queue.pop(0)
        if curr_game_state.solved():
            for move in curr_game_state.moves:
                print(move)
            return  # all done

        queue.extend(curr_game_state.execute_move())


# --------------------
# Better Implementation
# https://www.freecodecamp.org/news/analyzing-the-algorithm-to-solve-the-tower-of-hanoi-problem-686685f032e3/

# this class is just used as an enum
class Towers:
    peg_1 = 1
    peg_2 = 2
    peg_3 = 3


def solve_hanoi_redux(disks,source, inter, dest):
    if disks == 1:
        print("Move {} to {}".format(disks, dest))
    else:
        solve_hanoi_redux(disks-1, source, dest, inter)
        print("Move {} to {}".format(disks, dest))
        solve_hanoi_redux(disks-1, inter, source, dest)



if __name__ == '__main__':
    # puzzle = hanoi()
    # puzzle.add_discs(n=3)
    # solve_hanoi(puzzle)
    #
    # print("\n------\n")
    # puzzle = hanoi()
    # puzzle.add_discs(n=3)
    # solve_hanoi(puzzle)
    print("Disks=3")
    solve_hanoi_redux(3, Towers.peg_1, Towers.peg_2, Towers.peg_3)
    print('-------------')
    print("Disks=4")
    solve_hanoi_redux(4, Towers.peg_1, Towers.peg_2, Towers.peg_3)
    print('-------------')
    print("Disks=5")
    solve_hanoi_redux(5, Towers.peg_1, Towers.peg_2, Towers.peg_3)