
def get_int_list(filename):
    int_list = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            int_list.append(int(line))
    return int_list


def two_sum(int_list, target):
    s = set(int_list)
    for i in s:
        if target - i in s:
            print "Found {0}, {1}".format(i, target - i)
            return i * (target - i)
    return -1


def three_sum(int_list, target):
    for i in range(len(int_list)):
        for j in range(i+1, len(int_list)):
            for k in range(j+1, len(int_list)):
                if (int_list[i] + int_list[j] + int_list[k]) == target:
                    return int_list[i] * int_list[j] * int_list[k]
    return -1


int_list = get_int_list("input1.txt")
print(two_sum(int_list, 2020))
print(three_sum(int_list, 2020))