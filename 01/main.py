kcal_counter = []
current = 0
with open("data.txt", "r") as f:
    for line in f:
        try:
            current += int(line)
        except:
            kcal_counter.append(current)
            current = 0
kcal_counter.sort(reverse=True)
print(kcal_counter[0])
print(sum(kcal_counter[0:3]))