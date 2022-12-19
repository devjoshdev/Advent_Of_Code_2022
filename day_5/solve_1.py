line = '    [S] [C]         [Z]            '
line2 = '[F] [J] [P]         [T]     [N]    '

## process each line with sliding window?
crates = {x:[] for x in range(1,10)}

def process_line(line):
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

process_line(line)
process_line(line2)
print(crates)
