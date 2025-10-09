# BEFORE importing pyplot, you can force a GUI backend if needed:
# import matplotlib
# matplotlib.use("QtAgg")  # or "TkAgg" if Qt isn’t available

# from graph_viz import visualize_file
# import matplotlib.pyplot as plt
#
# fig, ax = visualize_file("input.txt", out_path=None, layout="spring")

with (open('input.txt', 'r') as f):
    n, m = map(int, f.readline().strip().split())

    new_graph = set()

    for i in range(m):
        first, second = map(int, f.readline().strip().split())
        if first != second:
            ordered_edge = tuple(sorted((first, second)))

            if ordered_edge not in new_graph:
                new_graph.add(ordered_edge)

print(n, len(new_graph))
for el in new_graph:
    print(el[0], el[1])