from dataclasses import dataclass
from typing import Optional

# from print_tree import display

@dataclass
class Node:
    key: int = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None

global ans
ans = None

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

def check_balance(l_height, r_height):
    global ans
    if abs(l_height - r_height) > 1:
        ans = False

def avl_balance(root):

    if root.left is not None:
        l_height = avl_balance(root.left)

    if root.right is not None:
        r_height = avl_balance(root.right)

    if root.right is None and root.left is None:
        return 0

    if root.left is None and root.right is not None:
        check_balance(0, r_height + 1)
        return r_height + 1

    if root.left is not None and root.right is None:
        check_balance(l_height + 1, 0)
        return l_height + 1

    if root.left is not None and root.right is not None:
        check_balance(l_height + 1, r_height + 1)
        return max(r_height, l_height) + 1


def is_avl_balanced(root: Optional[Node]) -> bool:
    def check(node: Optional[Node]) -> int:
        nonlocal balanced
        if node is None:
            return 0

        left_height = check(node.left)
        right_height = check(node.right)

        if abs(left_height - right_height) > 1:
            balanced = False

        return max(left_height, right_height) + 1

    balanced = True
    check(root)
    return balanced


root = None
for el in arr[:-1]:
    root, curr_height = add(root, el, 1)

# display(root)
# height = avl_balance(root)
# print(f'{height}')
# if ans is None:
#     print("YES")
# else:
#     print("NO")

if is_avl_balanced(root):
    print("YES")
else:
    print("NO")