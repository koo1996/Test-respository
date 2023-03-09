from base64 import b64decode  #decode
T = int(input())
for t in range(1, T + 1):
    data = input()
    ans = b64decode(data).decode('UTF-8')
    print(f'#{t} {ans}')