def range_to_int(r: str) -> int:
    res = 0
    start, end = r.split("-")
    for i in range(int(start), int(end)+1):
        res += 1<<i
    return res

full_overlaps = 0
overlaps = 0

with open("data.txt", "r") as f:
    for line in f:
        line = line.strip()
        p1, p2 = line.split(",")
        r1, r2 = range_to_int(p1), range_to_int(p2)
        if (r1 & r2 == r1) or (r1 & r2 == r2):
            full_overlaps += 1
        if r1 & r2:
            overlaps += 1

print(full_overlaps)
print(overlaps)