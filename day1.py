def calculate_fuel(input):
    return (input // 3) - 2


def calculate_additional_fuel(input):
    additional_fuel = calculate_fuel(input)
    total = additional_fuel
    while additional_fuel > 0:
        additional_fuel = calculate_fuel(additional_fuel)
        if additional_fuel > 0:
            total += additional_fuel

    return total

total = 0
file = open("inputfiles/day1.txt", "r")
lines = file.readlines()
for line in lines:
    #total += calculate_fuel(int(line))
    total += calculate_additional_fuel(int(line))

print(total)




