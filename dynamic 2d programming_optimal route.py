# Having a two-dimensional array (x columns, y rows). The array is filled with integers.
# Move from the top left element to the bottom right. Allowed movement: to the right and down.
# Find a path with the maximum sum of all cells, find a path with the minimum sum of all cells.
# Find total cost of each path.

from random import randint
from typing import Callable, List, Tuple


def print_route(raw_map: List[List[int]], coordinated_map: List[List[Tuple[int, int, int]]]):
    coords = coordinated_map[-1][-1][1]
    route = [(len(coordinated_map[0])-1, len(coordinated_map)-1), coords]  # add last item and coords in last item
    while coords != (0, 0):
        coords = coordinated_map[coords[1]][coords[0]][1]
        route.append(coords)
    for y, row in enumerate(raw_map):
        for x, item in enumerate(row):
            print(f'\033[32m{item:5}\033[0m' if (x, y) in route else f'{item:5}', end='')
        print()


def get_route_cost(comparator: Callable, raw_map: List[List[int]]) -> int:
    valued_map = []  # map with dynamic weights according comparator function and coordinates of previous point
    for x in range(len(raw_map[0])):
        for y in range(len(raw_map)):
            if len(valued_map)-1 < y:
                valued_map.append([])
            if x == y == 0:
                valued_map[y].append((raw_map[y][x], (0, 0)))
            elif y == 0:
                valued_map[0].append((raw_map[0][x]+valued_map[0][x-1][0], (x-1, 0)))
            elif x == 0:
                valued_map[y].append((raw_map[y][0]+valued_map[y-1][0][0], (0, y-1)))
            else:
                comparison = comparator(valued_map[y-1][x][0], valued_map[y][x-1][0])
                coords = (x, y-1) if comparison == valued_map[y-1][x][0] else (x-1, y)
                valued_map[y].append((raw_map[y][x] + comparison, coords))
    print_route(raw_map, valued_map)
    return valued_map[-1][-1][0]


COLUMNS = 20
ROWS = 10
map_ = [[randint(0, 99) for _ in range(COLUMNS)] for _ in range(ROWS)]
print('Generated map:')
# formatted output of print(*map_, sep='\n')
[print(f'{item:5}' if x < len(row)-1 else f'{item:5}\n', end='') for row in map_ for x, item in enumerate(row)]
print()
print('Route with maximum cost:')
print(f'Max route cost: {get_route_cost(max ,map_)}')
print()
print('Route with minimal cost:')
print(f'Min route cost: {get_route_cost(min ,map_)}')
