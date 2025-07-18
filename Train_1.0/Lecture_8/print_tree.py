def _display_aux(root):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if root.right is None and root.left is None:
        line = '%s' % root.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _display_aux(root.left)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _display_aux(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(root.left)
    right, m, q, y = _display_aux(root.right)
    s = '%s' % root.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2  

def display(root):
    '''https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python'''
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)


# Print family tree: each parent can have multiple children. Each children has only one parent
def _print_family_tree(node, prefix: str = "", is_last: bool = True) -> None:
    """Recursive helper that draws a Unix‑style tree with ├── / └── branches."""
    branch = "└── " if is_last else "├── "
    print(prefix + branch + str(node.key))

    # Prefix for this node’s children:
    new_prefix = prefix + ("    " if is_last else "│   ")
    last_index = len(node.children) - 1
    for idx, child in enumerate(node.children):
        _print_family_tree(child, new_prefix, idx == last_index)

def display_family_tree(root) -> None:
    """Public helper – just call display(root)."""
    _print_family_tree(root)