
def fully_contained(interval1, interval2):
    interval1_beginning, interval1_end = int(interval1.split("-")[0]), int(interval1.split("-")[1]) 
    interval2_beginning, interval2_end = int(interval2.split("-")[0]), int(interval2.split("-")[1])
    if interval1_beginning == interval2_beginning:
        return True
    if interval1_beginning > interval2_beginning:
        return interval2_end >= interval1_end
    else:
        return interval1_end >= interval2_end

ranges_contained = 0
with open("input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        interval1, interval2 = line.split(",")
        if fully_contained(interval1, interval2):
            # print(f"Found an overlap with {interval1} and {interval2}")
            ranges_contained += 1
        else:
            print(f"Did not find overlap with {interval1} and {interval2}")
print(f"Total: {ranges_contained}")


