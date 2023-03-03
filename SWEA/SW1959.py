T = int(input())

for tc in range(1, T+1):
    a_,b_ = map(int,input().split())    
    if a_>b_:
        max_ = a_
        min_ = b_        
        b_case = list(map(int,input().split()))
        a_case = list(map(int,input().split()))
    else:
        max_ = b_
        min_ = a_   
        a_case = list(map(int,input().split()))
        b_case = list(map(int,input().split()))
    
    for i in range(min_ + 1):
        max = 0
        for j in range(min_):
            max+= b_case[j] * a_case[j+i]
        a_list = []
        a_list.append(max)
    
    print("#{} {}".format(tc, max(a_list)))