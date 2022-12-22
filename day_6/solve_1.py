
idx = 0
found = False
with open("input.txt") as f:
    line = f.readline().strip()
    while idx+4 < len(line):
        slice = line[idx:idx+4]
        if len(set(slice)) == 4:
            print(f"Found marker at position {idx+4}, set of chars is {slice}")
            found = True
            break
        idx += 1

print("Error, was not able to find the marker") if not found else print("Success")

