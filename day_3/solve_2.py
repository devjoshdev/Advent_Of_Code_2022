from string import ascii_letters as LETTERS
PRIORITIES = {letter : idx + 1 for idx, letter in enumerate(LETTERS)}

def find_repeated_char(s1, s2, s3):
    for char in s1:
        if char in s2:
            if char in s3:
                return char, PRIORITIES[char]
    raise ValueError("No repeats!")

total_priority_of_item_type_that_shows_up_in_each_member_compartments = 0 ## hehe
with open("input.txt") as f:
    group = []
    for line in f:
        group.append(line)
        if len(group) == 3:
            char, priority = find_repeated_char(*group)
            total_priority_of_item_type_that_shows_up_in_each_member_compartments += priority
            print(f"Found character: {char}")
            print(f"Corresponding priority: {priority}")
            group.clear()
print(f"Total: {total_priority_of_item_type_that_shows_up_in_each_member_compartments}")
