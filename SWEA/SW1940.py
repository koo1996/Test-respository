T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sum = 0
    speed = 0
    for i in range(N):
        a,b = map(int,input().split())
        if b <= 2:
            if a == 1:
                sum = sum + b
                speed += sum
            elif a == 2:
                sum = sum - b
                speed += sum
            elif a == 0:
                speed += sum

    print("#{} {}".format(tc,speed))

    