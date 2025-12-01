def dial_solution(instructions):
    position = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "L":
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        if position == 0:
            zero_count += 1

    return zero_count


try:
    with open("input.txt", "r") as input:
        puzzle_input = [line.strip() for line in input if line.strip()]

    password = dial_solution(puzzle_input)
    print(f"Password: {password}")
except FileNotFoundError:
    print("Please save your puzzle input to 'input.txt'")
