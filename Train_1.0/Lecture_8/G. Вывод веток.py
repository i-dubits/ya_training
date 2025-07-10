from dataclasses import dataclass
from typing import Optional

# from print_tree import display

@dataclass
class Node:
    key: int = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


with (open('input.txt', 'r') as f):
    arr = list(map(int, f.readline().strip().split()))

def add(root: Node, key: int, curr_height) -> tuple[Node, int]:
    """
        Add element to tree

        Returns:
            Current root and the curr element height
    """

    if root is None:
        root = Node(key)
        return root, curr_height

    if key == root.key:
        return root, -1

    elif key < root.key:
        if root.left is not None:
            _, curr_height = add(root.left, key, curr_height + 1)
        else:
            new_node = Node(key, left=None, right=None, parent=root)
            root.left = new_node
            return root, curr_height + 1

    elif key > root.key:
        if root.right is not None:
            _, curr_height  = add(root.right, key, curr_height + 1)
        else:
            new_node = Node(key, left=None, right=None, parent=root)
            root.right = new_node
            return root, curr_height + 1

    return root, curr_height

def inorder_traversal_one_child(root):
    if root.left is not None:
        inorder_traversal_one_child(root.left)

    first_expr = root.right is None
    sec_expr = root.left is None

    if (first_expr and not sec_expr) or (not first_expr and sec_expr):
        print(root.key)

    if root.right is not None:
        inorder_traversal_one_child(root.right)




root = None
for el in arr[:-1]:
    root, curr_height = add(root, el, 1)

# display(root)
inorder_traversal_one_child(root)