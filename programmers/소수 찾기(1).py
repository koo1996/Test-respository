n = 10
answer = 0    
for i in range(2,n+1):
    cnt = 0
    for j in range(1,i+1):
        if i % j != 0:
            break
    answer += 1
    print(i)
print(answer)