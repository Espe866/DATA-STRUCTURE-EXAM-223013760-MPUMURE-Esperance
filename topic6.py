def create_tree_node(data):
    """Creates a tree node."""
    return {"data": data, "children": []}

def add_child(parent, child):
    """Adds a child to a parent node."""
    parent["children"].append(child)

def print_tree(node, level=0):
    """Recursively prints the tree structure."""
    print(" " * (level * 4) + str(node["data"]))
    for child in node["children"]:
        print_tree(child, level + 1)

# Example usage for hierarchical data in the library management system
if __name__ == "__main__":
    print("\n--- Tree Example ---")
    root = create_tree_node("Library")

    section_1 = create_tree_node("Programming")
    section_2 = create_tree_node("Data Science")

    add_child(root, section_1)
    add_child(root, section_2)

    book_1 = create_tree_node("Python Basics")
    book_2 = create_tree_node("Advanced Python")
    book_3 = create_tree_node("Data Structures")

    add_child(section_1, book_1)
    add_child(section_1, book_2)
    add_child(section_1, book_3)

    book_4 = create_tree_node("Machine Learning")
    book_5 = create_tree_node("Deep Learning")

    add_child(section_2, book_4)
    add_child(section_2, book_5)

    print("Library Hierarchical Structure:")
    print_tree(root)
