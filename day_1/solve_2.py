elves = []
top_three = []

with open("input.txt", "r") as f:
    current_total = 0
    for line in f:
        if line == "\n":
            elves.append(current_total)
            current_total = 0
        else:
            calories = int(line)
            current_total += calories

for i in range(3):
    current_max = max(elves)
    top_three.append(current_max)
    elves.remove(current_max)
    print(f"Number {i+1}: {current_max}")

print(f"Total: {sum(top_three)}")
