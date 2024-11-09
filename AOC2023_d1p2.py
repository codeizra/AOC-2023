# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

def calculate_calibration_value(line):
    digit_map = {
        "one":"1", 
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        "zero":"0"
    }

    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        for digit_str, digit_num in digit_map.items():
            if line[i:].startswith(digit_str):
                digits.append(digit_num)
                break
    return int(digits[0] + digits[-1])

def sum_calibration_values(lines):
    total_sum = 0
    for line in lines:
        total_sum += calculate_calibration_value(line)
    return total_sum

with open('input1_AOC2023.txt', 'r') as file:
    lines = file.readlines()

result = sum_calibration_values(lines)
print(result)