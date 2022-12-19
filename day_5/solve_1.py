line = '    [S] [C]         [Z]            '
line2 = '[F] [J] [P]         [T]     [N]    '

def process_move(line):
    pass


def process_line(line):
    print(f"Line to process: {line}")
    idx = 0
    tower = 1
    while idx < len(line):
        col = line[idx:idx+4]
        stripped = col.strip()
        if stripped == '':
            print('skipped', tower)
            tower += 1
            pass
        else:
            letter = stripped.split('[')[1][0]
            print(f"{letter}, not skipped {tower}")
            crates[tower].append(letter) 
            tower += 1
        idx += 4

## process each line with sliding window?
crates = {x:[] for x in range(1,10)}
parse_input = True
with open("input.txt", 'r') as f:
    for line in f:
        if parse_input:
            if line.startswith(' 1'):
                parse_input = False
            else:
                process_line(line)

        else:
            if line == '':
                pass
            else:
                process_move(line)
print(crates)

