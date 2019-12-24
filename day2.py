#input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"
input = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"

s_instructions = input.split(",")
instructions = list(map(lambda s: int(s), s_instructions))


def plus(start_pos):
    first_source_addr = instructions[start_pos + 1]
    second_source_addr = instructions[start_pos + 2]
    dest_addr = instructions[start_pos + 3]
    first_value = instructions[first_source_addr]
    second_value = instructions[second_source_addr]
    value = first_value + second_value
    instructions[dest_addr] = value


def multiply(start_pos):
    first_source_addr = instructions[start_pos + 1]
    second_source_addr = instructions[start_pos + 2]
    dest_addr = instructions[start_pos + 3]
    first_value = instructions[first_source_addr]
    second_value = instructions[second_source_addr]
    value = first_value * second_value
    instructions[dest_addr] = value


def handle_instruction(start_pos):
    opcode = instructions[start_pos]
    if opcode == 1:
        plus(start_pos)
        return True
    elif opcode == 2:
        multiply(start_pos)
        return True
    elif opcode == 99:
        return False
    else:
        print("invalid instruction")
        return False


def reset_memory():
    global s_instructions
    s_instructions = input.split(",")
    global instructions
    instructions = list(map(lambda s: int(s), s_instructions))


def test_run(noun, verb):
    done = False
    reset_memory()
    instruction_pointer = 0

    instructions[1] = noun
    instructions[2] = verb

    while not done:
        outcome = handle_instruction(instruction_pointer)
        instruction_pointer += 4
        if not outcome:
            done = True

    return instructions[0]


for n in range(0, 100):
    for v in range(0, 100):
        if n > len(instructions) or v > len(instructions):
            print("skipping")
        else:
            if test_run(n, v) == 19690720:
                opcode = 100 * n + v
                print(opcode)



