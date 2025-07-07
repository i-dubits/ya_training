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

max_height = 1
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


def find_max(root):
    if root.right is not None:
        return find_max(root.right)
    else:
        return root.key

def second_el(root, max_found):

    if max_found is False:
        if root.right is not None:
            return second_el(root.right, False)
        else:
            if root.left is None:
                return root.parent.key
            else:
                return second_el(root.left, True)

    else:
        if root.right is not None:
            return second_el(root.right, True)

        else:
            return root.key

def second_el_2(root):
    if root.right is not None:
        return second_el_2(root.right)

    if root.left is None:
        return root.parent.key
    else:
        return find_max(root.left)





root = None
for el in arr[:-1]:
    root, curr_height = add(root, el, 1)

# display(root)
# print(second_el(root, False))
print(second_el_2(root))