def create_node(data):
    return {"data": data, "prev": None, "next": None}
def create_doubly_linked_list():
    return None
def insert_at_end(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    current = head
    while current["next"] is not None:
        current = current["next"]
    current["next"] = new_node
    new_node["prev"] = current
    return head
def insert_at_beginning(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    new_node["next"] = head
    head["prev"] = new_node
    return new_node
def delete_node(head, key):
    if head is None:
        return head
    if head["data"] == key:
        new_head = head["next"]
        if new_head is not None:
            new_head["prev"] = None
        return new_head
    current = head
    while current is not None:
        if current["data"] == key:
            if current["prev"] is not None:
                current["prev"]["next"] = current["next"]
            if current["next"] is not None:
                current["next"]["prev"] = current["prev"]
            return head
        current = current["next"]
    return head
def search_doubly_linked_list(head, key):
    current = head
    while current is not None:
        if current["data"] == key:
            return True
        current = current["next"]
    return False
def print_doubly_linked_list(head):
    current = head
    while current is not None:
        print(f"{current['data']} <-> ", end="")
        current = current["next"]
    print("None")
def limit_doubly_linked_list(head, max_size):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current["next"]
    while count > max_size:
        head = delete_node(head, head["data"])
        count -= 1
    return head
if __name__ == "__main__":
    print("--- Doubly Linked List Example ---")
    orders = create_doubly_linked_list()

    orders = insert_at_end(orders, "Order 1: Python Programming")
    orders = insert_at_end(orders, "Order 2: Data Structures")
    orders = insert_at_end(orders, "Order 3: Algorithms")

    print("Initial orders:")
    print_doubly_linked_list(orders)

    orders = insert_at_beginning(orders, "Order 0: Introduction to CS")
    print("Orders after adding at the beginning:")
    print_doubly_linked_list(orders)

    orders = delete_node(orders, "Order 2: Data Structures")
    print("Orders after deleting 'Order 2: Data Structures':")
    print_doubly_linked_list(orders)

    max_orders = 3
    orders = limit_doubly_linked_list(orders, max_orders)
    print(f"Orders after limiting to {max_orders}:")
    print_doubly_linked_list(orders)

    print("Searching for 'Order 3: Algorithms':", search_doubly_linked_list(orders, "Order 3: Algorithms"))
    print("Searching for 'Order 4: Advanced Topics':", search_doubly_linked_list(orders, "Order 4: Advanced Topics"))
