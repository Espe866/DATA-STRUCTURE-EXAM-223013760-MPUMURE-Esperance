def create_node(data):
    return {"data": data, "next": None}
def create_linked_list():
    return None
def insert_at_end(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    current = head
    while current["next"] is not None:
        current = current["next"]
    current["next"] = new_node
    return head
def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node["next"] = head
    return new_node
def delete_node(head, key):
    if head is None:
        return head
    if head["data"] == key:
        return head["next"]
    current = head
    while current["next"] is not None:
        if current["next"]["data"] == key:
            current["next"] = current["next"]["next"]
            return head
        current = current["next"]
    return head

def search_linked_list(head, key):
    current = head
    while current is not None:
        if current["data"] == key:
            return True
        current = current["next"]
    return False

def print_linked_list(head):
    current = head
    while current is not None:
        print(current["data"], end=" -> ")
        current = current["next"]
    print("None")

# Example usage for linked list
if __name__ == "__main__":
    linked_list = create_linked_list()
    linked_list = insert_at_end(linked_list, "Book 1: Python Programming")
    linked_list = insert_at_end(linked_list, "Book 2: Data Structures")
    linked_list = insert_at_end(linked_list, "Book 3: Algorithms")
    print("Initial linked list:")
    print_linked_list(linked_list)
    linked_list = insert_at_beginning(linked_list, "Book 0: Introduction to CS")
    print("Linked list after adding a book at the beginning:")
    print_linked_list(linked_list)
    linked_list = delete_node(linked_list, "Book 2: Data Structures")
    print("Linked list after deleting 'Book 2: Data Structures':")
    print_linked_list(linked_list)
    print("Searching for 'Book 3: Algorithms':", search_linked_list(linked_list, "Book 3: Algorithms"))
    print("Searching for 'Book 4: Advanced Topics':", search_linked_list(linked_list, "Book 4: Advanced Topics"))
def create_node(data):
    return {"data": data, "next": None}

def create_linked_list():
    return None

def insert_at_end(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    current = head
    while current["next"] is not None:
        current = current["next"]
    current["next"] = new_node
    return head

def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node["next"] = head
    return new_node
def delete_node(head, key):
    if head is None:
        return head
    if head["data"] == key:
        return head["next"]
    current = head
    while current["next"] is not None:
        if current["next"]["data"] == key:
            current["next"] = current["next"]["next"]
            return head
        current = current["next"]
    return head
def search_linked_list(head, key):
    current = head
    while current is not None:
        if current["data"] == key:
            return True
        current = current["next"]
    return False
def print_linked_list(head):
    current = head
    while current is not None:
        print(current["data"], end=" -> ")
        current = current["next"]
    print("None")
if __name__ == "__main__":
    print("--- Linked List Example ---")
    linked_list = create_linked_list()

    linked_list = insert_at_end(linked_list, "Book 1: Python Programming")
    linked_list = insert_at_end(linked_list, "Book 2: Data Structures")
    linked_list = insert_at_end(linked_list, "Book 3: Algorithms")
    print("Initial linked list:")
    print_linked_list(linked_list)
    linked_list = insert_at_beginning(linked_list, "Book 0: Introduction to CS")
    print("Linked list after adding a book at the beginning:")
    print_linked_list(linked_list)
    linked_list = delete_node(linked_list, "Book 2: Data Structures")
    print("Linked list after deleting 'Book 2: Data Structures':")
    print_linked_list(linked_list)
    print("Searching for 'Book 3: Algorithms':", search_linked_list(linked_list, "Book 3: Algorithms"))
    print("Searching for 'Book 4: Advanced Topics':", search_linked_list(linked_list, "Book 4: Advanced Topics"))
