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


def safe_solution(instructions, debug=False):
    position = 50
    zero_count = 0

    if debug:
        print(f"Start at position {position}")

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        zeros_this_rotation = 0

        if direction == "R":
            if position == 0:
                first_hit = 100
            else:
                first_hit = 100 - position

            if distance >= first_hit:
                zeros_this_rotation = 1 + (distance - first_hit) // 100

            position = (position + distance) % 100

        else:
            if position == 0:
                first_hit = 100
            else:
                first_hit = position

            if distance >= first_hit:
                zeros_this_rotation = 1 + (distance - first_hit) // 100

            position = (position - distance) % 100

        zero_count += zeros_this_rotation

        if debug:
            print(
                f"{instruction}: position now {position}, zeros this rotation: {zeros_this_rotation}"
            )

    return zero_count


try:
    with open("input.txt", "r") as f:
        puzzle_input = [line.strip() for line in f if line.strip()]

    password_part1 = dial_solution(puzzle_input)
    password_part2 = safe_solution(puzzle_input)

    print(f"Part 1 Password: {password_part1}")
    print(f"Part 2 Password: {password_part2}")
except FileNotFoundError:
    print("Please save your puzzle input to 'input.txt'")
