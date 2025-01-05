def create_stack():
    return []
def push_stack(stack, item):
    stack.append(item)
def pop_stack(stack):
    if not is_stack_empty(stack):
        return stack.pop()
    else:
        return "Stack is empty."
def peek_stack(stack):
    if not is_stack_empty(stack):
        return stack[-1]
    else:
        return "Stack is empty."

def is_stack_empty(stack):
    return len(stack) == 0
def create_queue():
    return []
def enqueue(queue, item):
    queue.append(item)
def dequeue(queue):
    if not is_queue_empty(queue):
        return queue.pop(0)
    else:
        return "Queue is empty."
def front_queue(queue):
    if not is_queue_empty(queue):
        return queue[0]
    else:
        return "Queue is empty."
def is_queue_empty(queue):
    return len(queue) == 0
if __name__ == "__main__":
    print("\n Recently Accessed Books")
    book_stack = create_stack()
    push_stack(book_stack, "Book 1: Python Programming")
    push_stack(book_stack, "Book 2: Data Structures")
    push_stack(book_stack, "Book 3: Algorithms")
    
    print("books in the stack",book_stack)
    print("Top book in stack:", peek_stack(book_stack))
    print("Removing top book:", pop_stack(book_stack))
    print("Stack after removing top book:", book_stack)

    print("\n Borrowing Requests ")
    borrow_queue = create_queue()
    enqueue(borrow_queue, "Request 1: Borrow 'Machine Learning'")
    enqueue(borrow_queue, "Request 2: Borrow 'Artificial Intelligence'")
    enqueue(borrow_queue, "Request 3: Borrow 'Deep Learning'")

    print("all requested books",borrow_queue)
    print("Front request in queue:", front_queue(borrow_queue))
    print("Processing front request:", dequeue(borrow_queue))
    print("Queue after processing front request:", borrow_queue)
