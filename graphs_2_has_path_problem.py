#  acyclic directed graph
# depth / breadth first search
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=2733s
#
#       f --> g --> h
#       |   ^
#       v  /
#       i <-- j
#       |
#       v
#       k

# adjacency list
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path_dfs(graph, current, end):
    if current == end:
        return True
    for node in graph[current]:
        if has_path_dfs(graph, node, end):
            return True
    return False


def has_path_bfs(graph, start, end):
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        queue += graph[current]
    return False


print(has_path_dfs(graph, 'f', 'k'))
print(has_path_dfs(graph, 'j', 'f'))
print(has_path_bfs(graph, 'f', 'k'))
print(has_path_bfs(graph, 'j', 'f'))
