T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    space_ = ''
    for i in range(N):
        a,b = input().split()
        space_ += a*int(b)    
    print('#{}'.format(test_case))
    for j in range(1,len(space_)+1,10):
        print(space_[j-1:j+10-1])
