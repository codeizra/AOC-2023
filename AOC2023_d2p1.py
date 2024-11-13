def is_game_possible(game_info, max_red, max_green, max_blue):
    for subset in game_info:
        red, green, blue = 0, 0, 0
        for color_count in subset.split(", "):
            count, color = color_count.split()
            if color == "red" and int(count) > max_red:
                return False
            elif color == "green" and int(count) > max_green:
                return False
            elif color == "blue" and int(count) > max_blue:
                return False
    return True

def solve(input_file):
    total_id = 0
    with open(input_file, 'r') as f:
        for line in f:
            game_id, game_info = line.strip().split(": ")
            game_id = int(game_id.split()[1])
            if is_game_possible(game_info.split("; "), 12, 13, 14):
                total_id += game_id
    return total_id


if __name__ == "__main__":
    input_file = "input2_AOC2023.txt"
    result = solve(input_file)
    print(result)