elves = []


with open("input.txt", "r") as f:
    current_total = 0
    for line in f:
        if line == "\n":
            elves.append(current_total)
            current_total = 0
        else:
            calories = int(line)
            current_total += calories

print(f"Maximum Amount of Calories Held By One Elf: {max(elves)}")

