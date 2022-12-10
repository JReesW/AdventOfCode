with open("addenda/input08.txt", 'r') as file:
    lines = [[int(c) for c in line.strip()] for line in file.readlines()]


def part1():
    width, height = len(lines[0]), len(lines)
    grid = [[False for _ in range(width)] for _ in range(height)]

    for h in range(height):
        left, right = -1, -1
        for w in range(width):
            if (n := lines[h][w]) > left:
                grid[h][w] = True
                left = n
            if (n := lines[h][-(w+1)]) > right:
                grid[h][-(w+1)] = True
                right = n

    for w in range(width):
        top, bottom = -1, -1
        for h in range(height):
            if (n := lines[h][w]) > top:
                grid[h][w] = True
                top = n
            if (n := lines[-(h+1)][w]) > bottom:
                grid[-(h+1)][w] = True
                bottom = n

    return sum(row.count(True) for row in grid)


def part2():
    width, height = len(lines[0]), len(lines)
    highest = 0

    for h in range(height):
        for w in range(width):
            score = []

            s = 0
            for up in range(h-1, -1, -1):
                if lines[up][w] < lines[h][w]:
                    s += 1
                elif lines[up][w] >= lines[h][w]:
                    s += 1
                    break
            score.append(s)

            s = 0
            for down in range(h+1, height):
                if lines[down][w] < lines[h][w]:
                    s += 1
                elif lines[down][w] >= lines[h][w]:
                    s += 1
                    break
            score.append(s)

            s = 0
            for left in range(w - 1, -1, -1):
                if lines[h][left] < lines[h][w]:
                    s += 1
                elif lines[h][left] >= lines[h][w]:
                    s += 1
                    break
            score.append(s)

            s = 0
            for right in range(w + 1, width):
                if lines[h][right] < lines[h][w]:
                    s += 1
                elif lines[h][right] >= lines[h][w]:
                    s += 1
                    break
            score.append(s)

            if (n := score[0] * score[1] * score[2] * score[3]) > highest:
                highest = n

    return highest


print(part1())
print(part2())
