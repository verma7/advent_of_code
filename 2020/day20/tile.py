from collections import defaultdict


def read(filename):
    tiles = defaultdict(list)
    with open(filename) as f:
        for line in f.readlines():
            if "Tile" in line:
                tile_id = int(line.split(" ")[1].split(":")[0])
            elif line != "\n":
                tiles[tile_id].append(line.strip())
    return tiles


def part1(filename):
    tiles = read(filename)
    borders = defaultdict(list)
    for id, tile in tiles.items():
        borders[id].append(tile[0])
        borders[id].append(tile[-1])
        borders[id].append(''.join([line[0] for line in tile]))
        borders[id].append(''.join([line[-1] for line in tile]))
        borders[id].append(tile[0][::-1])
        borders[id].append(tile[-1][::-1])
        borders[id].append(''.join([line[0] for line in tile])[::-1])
        borders[id].append(''.join([line[-1] for line in tile])[::-1])
    print borders
    print len(tiles)
    print tiles
    s = set([i for id in tiles for i in borders[id]])
    print s
    print len(s)

    result = 1
    neigh = defaultdict(set)
    for id in tiles:
        for border in borders[id]:
            for i in tiles.keys():
                if id == i:
                    continue
                if border in borders[i]:
                    neigh[id].add(i)
        if len(neigh[id]) == 2:
            print id
            result *= id
    print neigh
    return result


print part1('input.txt')
