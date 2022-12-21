line = '    [S] [C]         [Z]            '
line2 = '[F] [J] [P]         [T]     [N]    '

def process_move(line):
    line = line.strip().split(" ")
    ops = [int(line[i]) for i in range(1, len(line), 2)]
    print(ops)



def process_line(line):
    idx = 0
    tower = 1
    while idx < len(line):
        col = line[idx:idx+4]
        stripped = col.strip()
        if stripped == '':
            tower += 1
            pass
        else:
            letter = stripped.split('[')[1][0]
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
            if line.strip() == '':
                pass
            else:
                process_move(line)

## TODO: to process_move, split by ' ' and find the numbers? 