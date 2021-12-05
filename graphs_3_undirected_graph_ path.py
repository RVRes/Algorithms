# we have to find path between nodes of undirect graph wich contains loops
from pprint import pprint
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=2733s
# represents bidirectional connections between nodes - we need to convert it to adjacency list
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['k', 'j'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]


#  graph (adjacency list - we created it from the edges list)
# graph = {
#  'i': ['j', 'k'],
#  'j': ['i', 'k'],
#  'k': ['i', 'j', 'm', 'l'],
#  'l': ['k'],
#  'm': ['k'],
#  'n': ['o'],
#  'o': ['n']
# }

# graph
#       i -- j
#       |  /
#       k -- l
#       |
#       m
#
#       o -- n

def make_adjacency_list(edges):
    graph = {}
    for nodeA, nodeB in edges:
        if nodeA not in graph:
            graph[nodeA] = []
        if nodeB not in graph:
            graph[nodeB] = []
        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)
    return graph


# ===========Recursive DFS==================
def undirected_graph_path_dfs_recursive(edges, start, end):
    graph = make_adjacency_list(edges)
    return has_path_DFS_recursive(graph, start, end, set())


def has_path_DFS_recursive(graph, current, end, visited) -> bool:
    if current in visited:
        return False
    visited.add(current)
    print(current)
    if current == end:
        return True
    for current_node in graph[current]:
        if has_path_DFS_recursive(graph, current_node, end, visited):
            return True
    return False


# ==============BFS==================
def undirected_graph_path_bfs(edges, start, end):
    graph = make_adjacency_list(edges)
    return has_path_bfs(graph, start, end)


def has_path_bfs(graph, start, end):
    queue = [start]
    visited = set()
    while queue:
        current_node = queue.pop(0)
        print(current_node)
        if current_node == end:
            return True
        visited.add(current_node)
        queue += filter(lambda x: (x not in visited) and (x not in queue), graph[current_node])
    return False


print('undirected_graph_path_dfs_recursive')
print(undirected_graph_path_dfs_recursive(edges, 'i', 'n'))
print(undirected_graph_path_dfs_recursive(edges, 'j', 'm'))
print('', 'undirected_graph_path_bfs', sep='\n')
print(undirected_graph_path_bfs(edges, 'i', 'n'))
print(undirected_graph_path_bfs(edges, 'j', 'm'))
