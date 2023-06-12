a = 3
d = 4
included = [true, false, false, true, true]
answer = 0
for i in range(len(included)):
    a += i * d
    if included[i] == "true":
        answer += a
print(answer)