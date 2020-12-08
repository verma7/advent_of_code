from collections import defaultdict


def get_graph(filename):
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    with open(filename) as f:
        for line in f.readlines():
            b = line.split(' bags contain ')
            src = b[0]
            dest = []
            if b[1].strip() != "no other bags.":
                for num_bag in b[1].split(','):
                    num_bag_l = num_bag.strip().split(' ')
                    dest_bag = num_bag_l[1] + " " + num_bag_l[2]
                    dest.append((int(num_bag_l[0]), dest_bag))
                    rev_graph[dest_bag].append(src)
            graph[src] = dest
    return graph, rev_graph


def dfs(bag, graph, visited):
    if bag in visited:
        return
    visited.add(bag)
    for container in graph[bag]:
        dfs(container, graph, visited)


def eventually_gold(filename):
    _, graph = get_graph(filename)
    print graph
    visited = set()
    dfs('shiny gold', graph, visited)
    print visited
    return len(visited) - 1


def dfs2(graph, bag):
    if not bag in graph:
        return 1
    total = 1
    for (count, contained) in graph[bag]:
        total += count * dfs2(graph, contained)
    print bag, total
    return total


def num_bags(filename):
    graph, _ = get_graph(filename)
    return dfs2(graph, 'shiny gold') - 1


print num_bags('input.txt')
