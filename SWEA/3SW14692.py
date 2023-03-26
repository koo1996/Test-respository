T = int(input())

for tc in range(1,T+1):
    qu = int(input())
    if qu % 2 == 1:
        print(f'#{tc} Bob')
    else:
        print(f'#{tc} Alice')
