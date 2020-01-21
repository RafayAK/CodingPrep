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

class hanoi:
    def __init__(self):
        self.peg_1 = []  # stack 1
        self.peg_2 = []  # stack 2
        self.peg_3 = []  # stack 3
        self.moves = []

    def add_discs(self, n):
        # add all the discs to peg_1

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
            if len(self.peg_3) == 0 or self.peg_3[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_1.pop(0)  # pick up disk
                new_state.peg_3.insert(0, disk)

        # see if discs from peg_2 can be moved:
        if self.peg_2:
            # pick first disk:
            disk = self.peg_2[0]
            # see if it can be moved to other two pegs
            if len(self.peg_1) == 0 or self.peg_1[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_2.pop(0)  # pick up disk
                new_state.peg_1.insert(0, disk)
            if len(self.peg_3) == 0 or self.peg_3[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_2.pop(0)  # pick up disk
                new_state.peg_3.insert(0, disk)

        # see if discs from peg_3 can be moved:
        if self.peg_3:
            # pick first disk:
            disk = self.peg_2[0]
            # see if it can be moved to other two pegs
            if len(self.peg_1) == 0 or self.peg_1[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_2.pop(0)  # pick up disk
                new_state.peg_1.insert(0, disk)
            if len(self.peg_3) == 0 or self.peg_3[0] > disk:
                new_state = deepcopy(self)
                disk = new_state.peg_2.pop(0)  # pick up disk
                new_state.peg_3.insert(0, disk)

    def __repr__(self):
        return "1:{}    , 2: {},    3:{}".format(self.peg_1, self.peg_2, self.peg_3)



def solve_hanoi(n):
    game = hanoi()
    game.add_discs(n)

    queue = []
    queue.append(game)

    while queue:
        curr_game_state = queue.pop(0)
        execute_move(curr_game_state)
