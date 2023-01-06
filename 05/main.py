import re
from copy import deepcopy

stack_count = 0
stacks: list[list[str]] = []
stacks2: list[list[str]] = []

insert_creates = True

with open("data.txt", "r") as f:
    for line in f:
        if not stack_count:
            stack_count = (len(line)+1)//4
            for _ in range(stack_count):
                stacks.append([])
                stacks2.append([])
        if insert_creates:
            if line[1] == "1":
                insert_creates = False
                continue
            for i in range(1, len(line), 4):
                if line[i] != " ":
                    stacks[i//4].insert(0, line[i])
                    stacks2[i//4].insert(0, line[i])

        else:
            line = line.strip()
            if not line:
                continue
            c, fr, t = re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
            c, fr, t = int(c), int(fr)-1, int(t)-1
            for _ in range(c):
                stacks[t].append(stacks[fr].pop())
            for item in stacks2[fr][-c:]:
                stacks2[t].append(item)
            for _ in range(c):
                stacks2[fr].pop()


print("".join([i[-1] for i in stacks]))
print("".join([i[-1] for i in stacks2]))