import multiprocessing as mp

# Today's an ugly one, lads


with open("addenda/input05.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    maps = []
    map_n = -1

    seeds = [int(n) for n in lines[0].strip().split(': ')[1].split(' ')]

    for line in lines[2:]:
        if len(line) == 0:
            continue
        if line[0].isalpha():
            map_n += 1
        else:
            if len(maps) == map_n:
                maps.append([])
            maps[map_n].append(tuple([int(n) for n in line.strip().split(' ')]))

    for m in maps:
        new_seeds = seeds[::]
        for d, s, l in m:
            for i, seed in enumerate(seeds):
                if s <= seed < (s + l):
                    new_seeds[i] = d + (seed - s)
        seeds = new_seeds[::]

    return min(seeds)


# my non-brute force solution which worked for the example, but not the actual input

# class Range:
#     def __init__(self, start, size, checked = False):
#         self.start = start
#         self.size = size
#         self.checked = checked
#
#     def __iter__(self):
#         return iter((self.start, self.size))
#
#     def __repr__(self):
#         return f"[{self.start}, {self.start + self.size})<{self.size}>"
#
#
# def part2():
# #     lines = """seeds: 79 14 55 13
# #
# # seed-to-soil map:
# # 50 98 2
# # 52 50 48
# #
# # soil-to-fertilizer map:
# # 0 15 37
# # 37 52 2
# # 39 0 15
# #
# # fertilizer-to-water map:
# # 49 53 8
# # 0 11 42
# # 42 0 7
# # 57 7 4
# #
# # water-to-light map:
# # 88 18 7
# # 18 25 70
# #
# # light-to-temperature map:
# # 45 77 23
# # 81 45 19
# # 68 64 13
# #
# # temperature-to-humidity map:
# # 0 69 1
# # 1 0 69
# #
# # humidity-to-location map:
# # 60 56 37
# # 56 93 4""".splitlines()
#     maps = []
#     map_n = -1
#
#     seeds = [int(n) for n in lines[0].strip().split(': ')[1].split(' ')]
#     seeds = [Range(seeds[n*2], seeds[n*2 + 1]) for n in range(len(seeds) // 2)]
#
#     for line in lines[2:]:
#         if len(line) == 0:
#             continue
#         if line[0].isalpha():
#             map_n += 1
#         else:
#             if len(maps) == map_n:
#                 maps.append([])
#             maps[map_n].append(tuple([int(n) for n in line.strip().split(' ')]))
#
#     # seeds = [Range(3, 6)]
#     # maps = [[(5, 5, 3), (2, 2, 4), (1, 1, 9), (6, 6, 4)]]
#
#     for m in maps:
#         new_seeds = []
#         for dest, source, length in m:
#             print(f"{Range(source, length)} -> {Range(dest, length)}")
#             remove = []
#             for seed in seeds:
#                 start, size = seed
#
#                 # only check unchecked seeds
#                 if not seed.checked:
#                     # if the seed's start is in the map range (B|C)
#                     print(f"{source} <= {start} < {source} + {length}")
#                     if source <= start < source + length:
#                         # if the seed is completely within the map range (C)
#                         print(f"{start} + {size} < {source} + {length}")
#                         if start + size < source + length:  # <= or just <  ???
#                             new_start = dest + (start - source)
#                             new_seeds.append(Range(new_start, size))
#                             remove.append(seed)
#                         # else if the start is within the range, but the end is not (B)
#                         else:
#                             new_start = dest + (start - source)
#                             new_size = (source + length) - start
#                             new_seeds.append(Range(new_start, new_size))
#
#                             rem_start = source + length
#                             rem_size = size - new_size
#                             seeds.append(Range(rem_start, rem_size))
#
#                             remove.append(seed)
#                     # elif ranges do not overlap
#                     elif (start < source and start + size < source) or (source + length <= start):
#                         continue  # new_seeds.append(seed)
#                     # else if the seed's start range is outside the map range (A|D)
#                     else:
#                         # if the seed's end is inside the map range (D)
#                         print(f"{start} + {size} < {source} + {length}")
#                         if start + size < source + length:
#                             new_start = dest
#                             new_size = size - (start - source)
#                             new_seeds.append(Range(new_start, new_size))
#
#                             rem_start = start
#                             rem_size = start - source
#                             seeds.append(Range(rem_start, rem_size))
#
#                             remove.append(seed)
#                         # else if the seed's end is outside the map range (A)
#                         else:
#                             new_start = dest
#                             new_size = length
#                             new_seeds.append(Range(new_start, new_size))
#
#                             rem_start_l = start
#                             rem_size_l = start - source
#                             seeds.append(Range(rem_start_l, rem_size_l))
#
#                             rem_start_r = source + length
#                             rem_size_r = size - new_size - rem_size_l
#                             seeds.append(Range(rem_start_r, rem_size_r))
#
#                             remove.append(seed)
#             for r in remove:
#                 seeds.remove(r)
#         for seed in seeds:
#             new_seeds.append(seed)
#             # add remaining seeds to new_seeds?
#         seeds = new_seeds[::]
#
#     return min(seeds, key=lambda s: s.start).start


# brute force

maps = []
map_n = -1

for line in lines[2:]:
    if len(line) == 0:
        continue
    if line[0].isalpha():
        map_n += 1
    else:
        if len(maps) == map_n:
            maps.append([])
        maps[map_n].append(tuple([int(n) for n in line.strip().split(' ')]))


seeds = [int(n) for n in lines[0].strip().split(': ')[1].split(' ')]
seeds = [(seeds[n*2], seeds[n*2 + 1]) for n in range(len(seeds) // 2)]


def from_map(m, val):
    for d, s, l in m:
        if d <= val < d + l:
            return s + (val - d)
    return val


def from_maps(val):
    for m in maps[::-1]:
        val = from_map(m, val)

    return val


def valid(seed):
    for s, sz in seeds:
        if s <= seed < s + sz:
            return True
    return False


def check_range(rnge):
    b, e = rnge
    for i in range(b, e):
        if i % 1_000_000 == 0:
            print(i)
        if valid(from_maps(i)):
            return i
    return None


def part2():
    with mp.Pool(mp.cpu_count() - 1) as p:
        res = p.map(check_range, [(n * 10_000_000, (n+1) * 10_000_000) for n in range(10, 20)])
    return [r for r in res if r is not None]


if __name__ == '__main__':
    print(part1())
    print(part2())
