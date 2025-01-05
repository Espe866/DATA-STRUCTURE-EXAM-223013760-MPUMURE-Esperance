from collections import deque

def create_deque():
    return deque()
def add_to_deque(deq, data):
    deq.append(data)
def add_to_front(deq, data):
    deq.appendleft(data)
def remove_from_deque(deq):
    if deq:
        return deq.pop()
    return None
def remove_from_front(deq):
    if deq:
        return deq.popleft()
    return None
def get_deque_contents(deq):
    return list(deq)
def is_deque_empty(deq):
    return len(deq) == 0
def limit_deque_size(deq, max_size):
    while len(deq) > max_size:
        deq.popleft()

if __name__ == "__main__":
    print("Deque")
    orders = create_deque()
    add_to_deque(orders, "Order 1: Python Programming")
    add_to_deque(orders, "Order 2: Data Structures")
    add_to_deque(orders, "Order 3: Algorithms")
    print("Current orders:", get_deque_contents(orders))
    add_to_front(orders, "Order 0: Introduction to CS")
    print("Orders after adding one to the front:", get_deque_contents(orders))
    remove_from_deque(orders)
    print("Orders after removing one from the end:", get_deque_contents(orders))
    remove_from_front(orders)
    print("Orders after removing one from the front:", get_deque_contents(orders))

    add_to_deque(orders, "Order 4: Advanced Topics")
    add_to_deque(orders, "Order 5: Machine Learning")
    print("Orders before limiting size:", get_deque_contents(orders))
    limit_deque_size(orders, 3)
    print("Orders after limiting size to 3:", get_deque_contents(orders))
    print("Is deque empty?:", is_deque_empty(orders))
