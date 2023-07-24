def solution(plans):
    for i in range(len(plans)):
        x,y = map(int,plans[i][1].split(':'))
        plans[i][1] = x * 60 + y 
    plans.sort(key = lambda x:x[1])
    print(plans)
    
    stack = []
    a,b,c = plans[0]
    print(a,b,c)  
    return stack