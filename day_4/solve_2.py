
def overlap(interval1, interval2):
    interval1_beginning, interval1_end = int(interval1.split("-")[0]), int(interval1.split("-")[1]) 
    interval2_beginning, interval2_end = int(interval2.split("-")[0]), int(interval2.split("-")[1])
    if interval1_beginning == interval2_beginning or interval1_end == interval2_end:
        return True
    if interval1_beginning > interval2_beginning:
        return interval2_beginning >= interval1_beginning or interval2_end >= interval1_beginning
    else:
        return interval1_beginning >= interval2_beginning or interval1_end >= interval2_beginning

overlaps = 0
with open("input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        interval1, interval2 = line.split(",")
        if overlap(interval1, interval2):
            # print(f"Found an overlap with {interval1} and {interval2}")
            overlaps += 1
        else:
            print(f"Did not find overlap with {interval1} and {interval2}")
print(f"Total: {overlaps}")


