"""
Implement a stack that has the following methods:

    - push(val), which pushes an element onto the stack
    - pop(), which pops off and returns the topmost element of the stack.
      If there are no elements in the stack, then it should throw an error or return null.
    - max(), which returns the maximum value in the stack currently.
      If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""

# push and pop in constant time no problem, but max can be a bit tricky
# idea:  create a list which store the max values encountered.
#        So, the last element of the list will be th most recent max encountered
#        when the pop value matches the last element of the max val, we also remove it from the
#        list. A catch could be if same value as the max is added to the stack, in that case also add to the max list

class stack:
    def __init__(self):
        self._stack_list = []
        self._max_list = []


    def length(self):
        return len(self._stack_list)

    def push(self, element):
        if self.length() == 0 :
            # empty stack, so add the new element to both the lists
            self._stack_list = [element] + self._stack_list
            self._max_list.append(element)
        else:
            # add to the stack list
            self._stack_list = [element] + self._stack_list
            # then check if is new max
            if element >= self._max_list[-1]:
                self._max_list.append(element)

    def pop(self):
        if self.length() > 0:
            val_to_pop = self._stack_list[0]
            self._stack_list = self._stack_list[1:]

            # check if popped value was the current max
            if val_to_pop == self._max_list[-1]:
                del self._max_list[-1]

            return val_to_pop
        else:
            return None #raise ValueError("Stack is empty")

    def max(self):
        if self.length() > 0:
            return self._max_list[-1]
        else:
            return None #raise ValueError("Stack is empty")

    def print(self):
        print("The current stack: {}".format(self._stack_list))



if __name__ == '__main__':
    s = stack()
    s.push(1)
    s.print()
    s.push(5)
    s.print()
    print("Max is : {}".format(s.max()))
    s.push(6)
    s.print()
    print("Max is : {}".format(s.max()))
    s.push(9)
    s.print()
    print("Max is : {}".format(s.max()))
    s.push(2)
    s.print()
    print("Max is : {}".format(s.max()))
    s.push(5)
    s.print()
    print("Max is : {}".format(s.max()))

    print("-----------------")

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))

    print("Popped: {}".format(s.pop()))
    s.print()
    print("Max is : {}".format(s.max()))



