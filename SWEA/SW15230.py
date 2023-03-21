T = int(input())

alp = 'abcdefghijklmnopqrstuvwxyz'
for tc in range(1,T+1):
    qu = input()
    cnt = 0
    for i in range(len(qu)):
        if alp[i] == qu[i]:
            cnt += 1
        else:
            break
    print(f'#{tc} {cnt}')
