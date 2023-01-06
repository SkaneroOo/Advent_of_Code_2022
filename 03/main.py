priorities = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s1 = 0

groups = []
s2 = 0

with open("data.txt", "r") as f:
    for line in f:
        line = line.strip()
        groups.append(line)
        p1 = line[:len(line)//2]
        p2 = line[len(line)//2:]
        for c in p1:
            if c in p2:
                s1 += priorities.index(c)
                break
        if len(groups) == 3:
            for c in groups[0]:
                if c in groups[1] and c in groups[2]:
                    s2 += priorities.index(c)
                    groups = []
                    break
print(s1)
print(s2)