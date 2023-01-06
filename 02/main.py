def calc_score(in1, in2):
    res = 0
    if in2 == "X":
        res = 1
        if in1 == "A":
            res += 3
        elif in1 == "C":
            res += 6
    elif in2 == "Y":
        res = 2
        if in1 == "A":
            res += 6
        elif in1 == "B":
            res += 3
    elif in2 == "Z":
        res = 3
        if in1 == "B":
            res += 6
        elif in1 == "C":
            res += 3
    return res

lookup1 = ["A", "B", "C"]
lookup2 = ["X", "Y", "Z"]

def true_calc_score(in1, in2):
    if in2 == "Y":
        return calc_score(in1, lookup2[lookup1.index(in1)])
    elif in2 == "Z":
        return calc_score(in1, lookup2[lookup1.index(in1)-2])
    else:
        return calc_score(in1, lookup2[lookup1.index(in1)-1])

score = 0
true_score = 0

with open("data.txt", "r") as f:
    for line in f:
        score += calc_score(*line.strip().split(" "))
        true_score += true_calc_score(*line.strip().split(" "))

print(score)
print(true_score)