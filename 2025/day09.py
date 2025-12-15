from itertools import combinations
import re

class Jump(Exception):
    """"""

with open("addenda/input09.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    corners = []
    for line in lines:
        x, y = tuple(map(int, line.split(',')))
        corners.append((x, y))
    
    largest = 0
    for (xa, ya), (xb, yb) in combinations(corners, 2):
        size = (abs(xa - xb) + 1) * (abs(ya - yb) + 1)
        if size > largest: largest = size

    return largest


def size(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def part2():
    corners = []
    xs, ys = [], []
    for line in lines:
        x, y = tuple(map(int, line.split(',')))
        corners.append((x, y))
        xs.append(x)
        ys.append(y)

    # Compress the X and Y coordinates of all the corners
    compress_x = {}
    for i, x in enumerate(sorted(set(xs))):
        compress_x[x] = i
        compress_x[i] = x  # bi-directional dict

    compress_y = {}
    for i, y in enumerate(sorted(set(ys))):
        compress_y[y] = i
        compress_y[i] = y  # idem
    
    # Setup a grid with the compressed corners
    grid = [[' ' for _ in range(compress_x[max(xs)]+1)] for _ in range(compress_y[max(ys)]+1)]
    for (xa, ya), (xb, yb) in zip(corners, [*corners[1:], corners[0]]):
        xa, xb = compress_x[xa], compress_x[xb]
        ya, yb = compress_y[ya], compress_y[yb]
        if xa == xb:
            for y in range(min(ya, yb), max(ya, yb)+1): grid[y][xa] = '#'
        if ya == yb:
            for x in range(min(xa, xb), max(xa, xb)+1): grid[ya][x] = '#'

    # Find a point inside the polygon
    seed = None
    for y, row in enumerate(grid):
        match = re.search(r'^ *# ', ''.join(row))
        if match:
            seed = match.end()-1, y
            break

    # Flood fill the grid
    queue = {seed}
    while queue:
        x, y = queue.pop()
        grid[y][x] = '.'
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if grid[ny][nx] == ' ':
                queue.add((nx, ny))
    
    # Find the largest rectangle that doesn't contain outside space
    largest_pair = None
    for (xa, ya), (xb, yb) in combinations(corners, 2):
        xa, xb = compress_x[xa], compress_x[xb]
        ya, yb = compress_y[ya], compress_y[yb]
        try:
            for x in range(min(xa, xb), max(xa, xb)+1):
                for y in range(min(ya, yb), max(ya, yb)+1):
                    if grid[y][x] == ' ': raise Jump
            if largest_pair is None or size(*largest_pair) < size((xa, ya), (xb, yb)):
                largest_pair = (xa, ya), (xb, yb)
        except Jump:
            continue

    # Decompress coords
    (xa, ya), (xb, yb) = largest_pair
    xa, xb = compress_x[xa], compress_x[xb]
    ya, yb = compress_y[ya], compress_y[yb]
    return size((xa, ya), (xb, yb))


print(part1())
print(part2())
