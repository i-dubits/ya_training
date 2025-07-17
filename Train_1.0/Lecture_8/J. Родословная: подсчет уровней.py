from dataclasses import dataclass, field
from typing import Optional

# from print_tree import display, display_family_tree
import sys
from collections import deque

sys.setrecursionlimit(100_000)

# Node for BST
@dataclass
class Node:
    key: int = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


# Node for genealogical tree
@dataclass
class Node_gen:
    key: str = None
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=list)
    height: int = 0

name_to_node = {}
root_node_candidates = set()

with (open('input.txt', 'r') as f):
    N = int(f.readline().strip())
    for i in range(N - 1):
        child_name, parent_name = f.readline().strip().split()

        # Process parent
        if parent_name in name_to_node:
            parent_node = name_to_node[parent_name]
        else:
            parent_node = Node_gen(parent_name, None)
            name_to_node[parent_name] = parent_node

            root_node_candidates.add(parent_name)

        # Process child
        if child_name in name_to_node:
            child_node = name_to_node[child_name]
        else:
            child_node = Node_gen(child_name, parent_node)
            name_to_node[child_name] = child_node

        # Add child to parent
        parent_node.children.append(child_node)
        # Add parent to child
        child_node.parent = parent_node
        if child_name in root_node_candidates:
            root_node_candidates.remove(child_name)


def pre_order_trav(root: Node_gen):
    if root.parent is None:
        root.height = 0
    else:
        root.height = root.parent.height + 1

    for child in root.children:
        pre_order_trav(child)


def pre_order_trav_iterative(root: Node_gen):

    queue = deque([root])
    level_number = 0

    while queue:
        number_el_on_level = len(queue)
        for _ in range(number_el_on_level):
            curr_node = queue.popleft()
            curr_node.height = level_number

            for child in curr_node.children:
                queue.append(child)

        level_number += 1

root = name_to_node[next(iter(root_node_candidates))]
# display_family_tree(root)
# pre_order_trav(root)
pre_order_trav_iterative(root)


for name in sorted(name_to_node):
    node = name_to_node[name]
    print(f'{name} {node.height}')






