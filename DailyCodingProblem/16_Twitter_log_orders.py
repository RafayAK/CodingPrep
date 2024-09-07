'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last
N order ids in a log. Implement a data structure to accomplish this,
with the following API:

    - record(order_id): adds the order_id to the log
    - get_last(i): gets the ith last element from the log.
      i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible
'''

class OrderLog:
    def __init__(self, N):
        self._order_ids = []
        self._log_max_size = N

    def record(self, order_id):
        if self._order_ids.__len__() == self._log_max_size:
            self._order_ids.pop(0)
        self._order_ids.append(order_id)

    def get_last(self, i):
        if i == 0:
            return []

        return self._order_ids[self._order_ids.__len__()-i]

    def showlog(self):
        print(self._order_ids)

if __name__ == '__main__':
    N = 5
    o = OrderLog(N)
    choice = -1

    print("1. Record\n2. Get Last\n3. Show log\n4. Exit")

    while True:

        choice = int(input("\nEnter your choice:").strip())

        if choice == 1:
            orderID = int(input("Enter the order ID:").strip())
            o.record(orderID)

        elif choice == 2:
            position = int(input("Enter the position").strip())
            print(o.get_last(position))

        elif choice == 3:
            o.showlog()

        elif choice == 4:
            exit(0)

        else:
            print("Invalid choice.")