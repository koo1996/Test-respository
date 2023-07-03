# AN / CF / MJ / RT / NA 
# 5 3 2 7 5
# N 1 
# C 1
# M 2
# T 3
# A 1

# R T
# C F
# J M
# A N
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

per = ["R", "T", "C", "F", "J", "M", "A", "N"]
score = [0 for _ in range(8)]
answer = ''
for i in survey:
    for j in i:
        if j in per:
            score[per.index(j)] += 1
print(score)