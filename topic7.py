import re

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
def bucket_sort(head, max_priority):
    buckets = [[] for _ in range(max_priority + 1)]
    current = head
    while current is not None:
        match = re.search(r"Priority (\d+)", current["data"])
        if match:
            priority = int(match.group(1)) 
            buckets[priority].append(current["data"])
        current = current["next"]
    new_head = None
    for bucket in buckets:
        for data in bucket:
            new_head = insert_at_end(new_head, data)
    
    return new_head

if __name__ == "__main__":
    print("--- Doubly Linked List Example with Bucket Sort ---")
    orders = create_doubly_linked_list()
    orders = insert_at_end(orders, "Order 3: Priority 2")
    orders = insert_at_end(orders, "Order 1: Priority 1")
    orders = insert_at_end(orders, "Order 2: Priority 3")
    print("Initial orders:")
    print_doubly_linked_list(orders)
    max_priority = 3 
    orders = bucket_sort(orders, max_priority)

    print("Orders after sorting by priority:")
    print_doubly_linked_list(orders)
