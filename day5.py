from enum import Enum

class Opcode(Enum):
    PLUS = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    COMPLETE = 99


class ParameterMode(Enum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1


input = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,40,93,224,1001,224,-3720,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,56,23,225,1102,64,78,225,1102,14,11,225,1101,84,27,225,1101,7,82,224,1001,224,-89,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1,35,47,224,1001,224,-140,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,75,90,225,101,9,122,224,101,-72,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1102,36,63,225,1002,192,29,224,1001,224,-1218,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,102,31,218,224,101,-2046,224,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1001,43,38,224,101,-52,224,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1102,33,42,225,2,95,40,224,101,-5850,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,37,66,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,344,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,494,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,509,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,108,226,677,224,1002,223,2,223,1005,224,644,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226"
#input = "1002,4,3,4,33"
system_id = "1"
instructions = input.split(",")
#instructions = list(map(lambda s: int(s), s_instructions))


def next_mode_flag(flags, current_flag_pointer):
    if len(flags) > current_flag_pointer:
        return flags[current_flag_pointer]
    else:
        return 0


def next_value(ip, mode_flags, mode_flag_pointer):
    operand = int(instructions[ip])
    # We assume that this is IMMEDIATE_MODE and use the raw value
    value = operand
    mode_flag = next_mode_flag(mode_flags, mode_flag_pointer)
    if mode_flag == ParameterMode.POSITION_MODE.value:
        # fetch the value located at first_operand position
        value = int(instructions[operand])

    return value


def handle_instruction():
    global instruction_pointer
    instruction_pointer
    instruction = instructions[instruction_pointer]
    mode_flags = []
    mode_flag_pointer = 0
    if len(instruction) > 2:
        # we need to split the instruction into mode and opcode
        # last two bits are the opcode
        s_opcode = instruction[-2:]

        # mode is from position - 2 and backwards
        first = len(instruction) - 2
        mode_flags = instruction[:first]
        mode_flags = list(map(lambda s: int(s), mode_flags[::-1]))
    else:
        s_opcode = instruction

    opcode = int(s_opcode)

    if opcode == Opcode.PLUS.value:
        # first value
        instruction_pointer += 1
        first_value = next_value(instruction_pointer, mode_flags, mode_flag_pointer)

        # second value
        instruction_pointer += 1
        mode_flag_pointer += 1
        second_value = next_value(instruction_pointer, mode_flags, mode_flag_pointer)
        result = first_value + second_value

        # destination
        instruction_pointer += 1
        destination = int(instructions[instruction_pointer])

        # and store
        instructions[destination] = str(result)

        instruction_pointer += 1
        return True
    elif opcode == Opcode.MULTIPLY.value:
        # first value
        instruction_pointer += 1
        first_value = next_value(instruction_pointer, mode_flags, mode_flag_pointer)

        # second value
        instruction_pointer += 1
        mode_flag_pointer += 1
        second_value = next_value(instruction_pointer, mode_flags, mode_flag_pointer)
        result = first_value * second_value

        # destination
        instruction_pointer += 1
        destination = int(instructions[instruction_pointer])

        # and store
        instructions[destination] = str(result)

        instruction_pointer += 1
        return True
    elif opcode == Opcode.INPUT.value:
        # advance
        instruction_pointer += 1
        address = int(instructions[instruction_pointer])
        instructions[address] = system_id
        instruction_pointer += 1
        return True
    elif opcode == Opcode.OUTPUT.value:
        #advance
        instruction_pointer += 1
        address = int(instructions[instruction_pointer])
        output = instructions[address]
        print("output: " + output)
        instruction_pointer += 1
        return True
    elif opcode == Opcode.COMPLETE.value:
        print("done")
        return False
    else:
        raise NotImplemented


# lets go
instruction_pointer = 0
cont = True
while cont:
    cont = handle_instruction()



