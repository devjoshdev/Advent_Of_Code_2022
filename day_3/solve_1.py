from string import ascii_letters as LETTERS
PRIORITIES = {letter : idx + 1 for idx, letter in enumerate(LETTERS)}

def find_repeated_char(s1, s2):
    for char in s1:
        if char in s2:
            return char, PRIORITIES[char]
    raise ValueError("No repeats!")

total_priority_of_item_type_that_shows_up_in_both_compartments = 0 ## hehe
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        first_half, second_half = line[0:len(line) // 2], line[len(line) // 2:]
        char, priority = find_repeated_char(first_half, second_half)
        total_priority_of_item_type_that_shows_up_in_both_compartments += priority
        print(f"Found character: {char}")
        print(f"Corresponding priority: {priority}")
print(f"Total: {total_priority_of_item_type_that_shows_up_in_both_compartments}")
