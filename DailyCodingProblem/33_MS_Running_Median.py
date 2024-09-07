"""
Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""


class minHeap:
    def __init__(self):
        self._heap = []

    def _has_parent(self, idx):
        if (idx-1)/2 < 0:
            return False
        else:
            return True

    def _has_left_child(self,idx):
        if (idx*2) +1 > self.get_len() -1:
            return False
        else:
            return True

    def _has_right_child(self,idx):
        if (idx*2) +2 > self.get_len() -1:
            return False
        else:
            return True

    def get_parent_idx(self, idx):
        return (idx-1)//2

    def _get_left_child_idx(self ,idx):
            return (idx*2) +1

    def _get_right_child_idx(self, idx):
            return (idx * 2) + 2


    def parent(self,idx):
        return self._heap[(idx-1)//2]

    def left_child(self, idx):
        return self._heap[(idx * 2) + 1]

    def right_child(self, idx):
        return self._heap[(idx * 2) + 2]

    def is_empty(self):
        if len(self._heap) == 0:
            return True
        else:
            return False

    def get_len(self):
        return len(self._heap)

    def _swap(self, idxA, idxB):
        self._heap[idxA], self._heap[idxB] = self._heap[idxB], self._heap[idxA]

    def peak(self):
        return self._heap[0]

    def pop(self):
        item = self._heap[0]

        # remove last element and set it to root
        self._heap[0] = self._heap[-1]
        self._heap = self._heap[:-1]
        self._heapifyDown()  # make sure everything is in correct order

        return item

    def add(self, element):
        # add element to the end of the list
        self._heap.append(element)
        self._heapifyUp()

    def _heapifyDown(self):
        index = 0

        while self._has_left_child(index):
            smaller_child_idx = self._get_left_child_idx(index)
            if self._has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_idx = self._get_right_child_idx(index)

            if self._heap[index] < self._heap[smaller_child_idx]:
                break # heap in order
            else:
                self._swap(index, smaller_child_idx)
                index = smaller_child_idx

    def _heapifyUp(self):
        index = len(self._heap) -1
        while self._has_parent(index) and self.parent(index) > self._heap[index]:
            parent_idx = self.get_parent_idx(index)
            self._swap(parent_idx, index )
            index = parent_idx


class maxHeap:
    def __init__(self):
        self._heap = []

    def _has_parent(self, idx):
        if (idx-1)/2 < 0:
            return False
        else:
            return True

    def _has_left_child(self,idx):
        if (idx*2) +1 > self.get_len() -1:
            return False
        else:
            return True

    def _has_right_child(self,idx):
        if (idx*2) +2 > self.get_len() -1:
            return False
        else:
            return True

    def get_parent_idx(self, idx):
        return (idx-1)//2

    def _get_left_child_idx(self ,idx):
            return (idx*2) +1

    def _get_right_child_idx(self, idx):
            return (idx * 2) + 2


    def parent(self,idx):
        return self._heap[(idx-1)//2]

    def left_child(self, idx):
        return self._heap[(idx * 2) + 1]

    def right_child(self, idx):
        return self._heap[(idx * 2) + 2]

    def is_empty(self):
        if len(self._heap) == 0:
            return True
        else:
            return False

    def get_len(self):
        return len(self._heap)

    def _swap(self, idxA, idxB):
        self._heap[idxA], self._heap[idxB] = self._heap[idxB], self._heap[idxA]

    def peak(self):
        return self._heap[0]

    def pop(self):
        item = self._heap[0]

        # remove last element and set it to root
        self._heap[0] = self._heap[-1]
        self._heap = self._heap[:-1]
        self._heapifyDown()  # make sure everything is in correct order

        return item

    def add(self, element):
        # add element to the end of the list
        self._heap.append(element)
        self._heapifyUp()

    def _heapifyDown(self):
        index = 0

        while self._has_left_child(index):
            smaller_child_idx = self._get_left_child_idx(index)
            if self._has_right_child(index) and self.right_child(index) > self.left_child(index):
                smaller_child_idx = self._get_right_child_idx(index)

            if self._heap[index] > self._heap[smaller_child_idx]:
                break # heap in order
            else:
                self._swap(index, smaller_child_idx)
                index = smaller_child_idx

    def _heapifyUp(self):
        index = len(self._heap) -1
        while self._has_parent(index) and self.parent(index) < self._heap[index]:
            parent_idx = self.get_parent_idx(index)
            self._swap(parent_idx, index )
            index = parent_idx


def running_median(arr):
    min_heap = minHeap()
    max_heap = maxHeap()

    for element in arr:
        min_heap.add(element)

        if min_heap.get_len() > max_heap.get_len()+1:  # if size diff b/w min_heap > 1
            temp = min_heap.pop()
            max_heap.add(temp)

        if min_heap.get_len() == max_heap.get_len():
            # print running median
            print((min_heap.peak()+max_heap.peak())/2)

        else:
            # odd sized list
            print(min_heap.peak())




if __name__ == '__main__':
    arr = [2, 1, 5, 7, 2, 0, 5]
    running_median(arr)