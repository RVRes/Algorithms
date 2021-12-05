#   DFT - depth first traversal - в одну сторону до конца
#       stack - last in, first out
#       pop - take last element, + - add list to another list
#
#   BFT - breadth first traversal - равномерно во все стороны
#       queue - first in first out
#       pop(0) - take first, + - add list to another list
#
#   Greph - direct, inderect
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=2733s
#
#
#   a --> c
#   |     |
#   v     V
#   b --> e
#   |
#   v
#   d <-- f

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': [],
    'e': [],
    'f': ['d']
}


def depth_first_traversal(graph: dict, start_point: str):
    stack = [start_point]
    while stack:
        current = stack.pop()
        stack += graph[current]
        print(current)


def depth_first_traversal_recursive(graph: dict, current: str):
    print(current)
    for point in graph[current]:
        depth_first_traversal_recursive(graph, point)


def breadth_first_traversal(graph: dict, start_point: str):
    queue = [start_point]
    while queue:
        current = queue.pop(0)
        queue += graph[current]
        print(current)


depth_first_traversal(graph, 'a')
print()
breadth_first_traversal(graph, 'a')
print()
depth_first_traversal_recursive(graph, 'a')
