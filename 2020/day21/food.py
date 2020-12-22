def read_ingredients_and_allergens(filename):
    ingredients = []
    allergens = {}
    with open(filename) as f:
        for line in f.readlines():
            l = line.split("(contains ")
            ing = l[0].strip().split(' ')
            ingredients.extend(ing)
            ings = set(ing)
            als = l[1].split(')')[0].split(', ')
            for al in als:
                if al in allergens:
                    allergens[al] = allergens[al].intersection(ings)
                else:
                    allergens[al] = ings
    return ingredients, allergens


def part1(filename):
    ingredients, allergens = read_ingredients_and_allergens(filename)
    print allergens
    ings_with_al = set()
    for i in allergens.values():
        ings_with_al = ings_with_al.union(i)
    count = 0
    for i in ingredients:
        if i not in ings_with_al:
            count += 1
    return count


def part2(filename):
    ingredients, allergens = read_ingredients_and_allergens(filename)
    cont = True
    print allergens
    while cont:
        cont = False
        for a, i in allergens.items():
            if len(i) == 1 and isinstance(i, set):
                allergens[a] = i.pop()
                for al in allergens.keys():
                    if isinstance(allergens[al], set):
                        allergens[al].discard(allergens[a])
            elif len(i) > 1 and isinstance(i, set):
                cont = True
        print allergens

    result = []
    for k in sorted(allergens.keys()):
        result.append(allergens[k])
    return ','.join(result)


print part2('input.txt')
