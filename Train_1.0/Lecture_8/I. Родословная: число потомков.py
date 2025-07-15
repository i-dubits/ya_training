from dataclasses import dataclass, field
from typing import Optional

# from print_tree import display, display_family_tree
import sys

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
    number_of_descendant: int = 0


def calc_desc(root: Node_gen):
    if not root.children:
        root.number_of_descendant = 0
        return 0
    else:
        total_number_of_children = 0
        for child in root.children:
            total_number_of_children += calc_desc(child) + 1
        root.number_of_descendant = total_number_of_children
        return total_number_of_children

def calc_desc_iterative(root: Node_gen):

    processed = False
    stack = [[root, processed]]

    while stack:
        curr_node, processed = stack[-1]
        if not processed:
            if curr_node.children:
                add_pos = 0
                for child in curr_node.children:
                    add_pos += 1
                    stack.append([child, False])

                stack[-(1 + add_pos)][1] = True
            else:
                stack[-1][1] = True

        else:
            if curr_node.children:
                for child in curr_node.children:
                    curr_node.number_of_descendant += child.number_of_descendant + 1
            stack.pop()

def calc_desc_iterative_two_stacks(root: Node_gen):
    traversal_stack = [root]
    post_order_stack = []

    while traversal_stack:
        curr_node = traversal_stack.pop()
        post_order_stack.append(curr_node)
        if curr_node.children:
            for child in curr_node.children:
                traversal_stack.append(child)

    while post_order_stack:
        curr_node = post_order_stack.pop()
        if curr_node.children:
            for child in curr_node.children:
                curr_node.number_of_descendant += child.number_of_descendant + 1


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


root = name_to_node[next(iter(root_node_candidates))]
# display_family_tree(root)
# calc_desc(root)
# calc_desc_iterative(root)
calc_desc_iterative_two_stacks(root)


for name in sorted(name_to_node):
    node = name_to_node[name]
    print(f'{name} {node.number_of_descendant}')






