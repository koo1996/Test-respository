T = int(input())

for tc in range(1,T+1):
    qu = input()
    cnt = 0
    for i in range(len(qu)-1):
        if qu[i]+qu[i+1] == '(|' or qu[i]+qu[i+1] == '|)' or qu[i]+qu[i+1] == '()':
            cnt += 1
    print(f'#{tc} {cnt}')