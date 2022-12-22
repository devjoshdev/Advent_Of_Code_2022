idx = 0
found = False
with open("input.txt") as f:
    line = f.readline().strip()
    while idx+14 < len(line):
        slice = line[idx:idx+14]
        if len(set(slice)) == 14:
            print(f"Found marker at position {idx+14}, set of chars is {slice}")
            found = True
            break
        idx += 1

print("Error, was not able to find the marker") if not found else print("Success")

