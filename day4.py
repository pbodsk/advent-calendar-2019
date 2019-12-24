lower_range = 382345
upper_range = 843167

password_length = 6

valid_candidates = []
final_valid_candidates = []


def digits_are_ascending(number):
    is_valid = True
    for pos in range(0, len(number) - 1):
        if number[pos + 1] < number[pos]:
            is_valid = False

    return is_valid


def two_of_the_same(number):
    #convert to a set so we know what digits we have
    values = set(number)
    groups = []
    for num in values:
        groups.append(number.count(num))

    return max(groups) >= 2


#print(only_two_of_the_same([1,1,1,1,2,2]))

#groups = ["123112".count(ch) for ch in set("123112")]
#print(groups)

for candidate in range(lower_range, upper_range + 1):
    s_candidate = str(candidate)
    if len(s_candidate) != password_length:
        raise ValueError

    two_of_the_same(s_candidate)

    if digits_are_ascending(s_candidate) and two_of_the_same(s_candidate):
        valid_candidates.append(s_candidate)

print(len(valid_candidates))

final_valid_candidates = []

for candidate in valid_candidates:
    digits = {}
    for chars in candidate:
        digits[chars] = candidate.count(chars)

    if 2 in digits.values():
        final_valid_candidates.append(candidate)

print(len(final_valid_candidates))



