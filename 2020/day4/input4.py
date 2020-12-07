import re
from collections import defaultdict


def read_input(filename):
    passports = []
    with open(filename) as f:
        lines = f.readlines()
        passport = defaultdict(str)
        for line in lines:
            fields = line.split()
            if fields:
                for field in fields:
                    kv = field.split(':')
                    passport[kv[0]] = kv[1]
            else:
                passports.append(passport)
                passport = defaultdict(str)
        passports.append(passport)
    return passports


def is_valid_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print passport
    for f in required_fields:
        if not passport[f]:
            print "Invalid passport: Absent field: ", f
            return False
    print "Valid passport"
    return True


def is_valid_passport_part2(passport):
    print passport
    date_valid = re.match(R'^\d{4}$', passport['byr']) and 1920 <= int(passport['byr']) <= 2002 and (
            re.match(R'^\d{4}$', passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020) and (
                         re.match(R'^\d{4}$', passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030)

    height_valid = False
    h1 = re.match(R'^(?P<height_in>\d+)in$', passport['hgt'])
    if h1:
        height_valid |= (59 <= int(h1.group('height_in')) <= 76)
    h2 = re.match(R'^(?P<height_cm>\d+)cm$', passport['hgt'])
    if h2:
        height_valid |= (150 <= int(h2.group('height_cm')) <= 193)

    rest_valid = re.match(R'^#[0-9a-f]{6}$', passport['hcl']) and (
        re.match(R'^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl'])) and (
                     re.match(R'^\d{9}$', passport['pid']))

    print "date: ", str(date_valid), " height: ", str(height_valid), " rest: ", str(rest_valid)
    return date_valid and height_valid and rest_valid


def count_valid_passports(filename):
    passports = read_input(filename)
    count = 0
    for passport in passports:
        if is_valid_passport_part2(passport):
            count += 1
    return count


print count_valid_passports("input4.txt")
