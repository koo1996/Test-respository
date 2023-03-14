T = int(input())

for tc in range(1,T+1):
    qu = input()
    cnt = 0
    for i in range(len(qu)):
        if qu[i] == '(':
            if qu[i+1] == '|':
                cnt += 1
            elif qu[i+1] == ')':
                cnt += 1
            else:
                break
        elif qu[i] == '|':
            if qu[i+1] == ')':
                cnt += 1
            else:
                break
        else:
            break
    print(f'#{tc} {cnt}')