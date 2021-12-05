# count islands
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=2733s
# w - represents water, l - represents land
#
#       w l w w l w
#       l l w w l w
#       w l w w w w
#       w w w l l w
#       w l w l l w
#       w w w w w w

graph = [
    ['w', 'l', 'w', 'w', 'l', 'w'],
    ['l', 'l', 'w', 'w', 'l', 'w'],
    ['w', 'l', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'l', 'w'],
    ['w', 'l', 'w', 'l', 'l', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w']
]


def count_islands(graph):
    visited = set()
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'l' and coord_to_str(i, j) not in visited:
                explore(graph, (i, j), visited)
                count += 1
    return count


# because we cant find pointers to (i, j) within set
def coord_to_str(x, y):
    return f'{x}_{y}'


def explore(graph, coord, visited):
    i, j = coord
    if i < 0 or i > len(graph) - 1 or j < 0 or j > len(graph[i]) - 1 or graph[i][j] == 'w' or coord_to_str(
            *coord) in visited:
        return
    visited.add(coord_to_str(*coord))
    explore(graph, (i - 1, j), visited)
    explore(graph, (i + 1, j), visited)
    explore(graph, (i, j - 1), visited)
    explore(graph, (i, j + 1), visited)


print(count_islands(graph))
