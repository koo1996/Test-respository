T  = int(input())

for tc in range(1,T+1):
    qu = int(input())
    for i in range(1,10):
        if qu % i == 0:
            result = qu / i
            if result <= 9:
                answer = 'Yes'
                break
            else:
                answer = 'No'
    print(f'#{tc} {answer}')