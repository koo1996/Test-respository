def solution(progresses, speeds):
    answer = []
    work = []
    stack = []
    for i in range(len(progresses)): #진도율 계산 
        a = 100 - progresses[i]
        if a % speeds[i] == 0: #남은 진도율에서 speeds로 나누어 떨어지면 몫을 work 리스트에 추가
            work.append(a//speeds[i])
        else:
            work.append((a//speeds[i])+1) #나누어 떨어지지 않으면 몫+1 을 work 리스트에 추가

    stack.append(work[0]) #stack에 work[0]을 추가
    for j in range(1,len(work)): 

        if stack[0] >= work[j]: #stack[0]이 work[j]보다 크거나 같으면 work[j]를 stack에 추가
            stack.append(work[j]) 
        else:
            answer.append(len(stack))
            stack = []
            stack.append(work[j])
    answer.append(len(stack))            
    return answer