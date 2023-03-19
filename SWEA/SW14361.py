T = int(input())

for tc in range(1,T+1): # 테스트케이스 
    qu = input() 
    qu_list = sorted(list(qu)) # 입력값 정렬해서 list에 저장
    sum = 0 # sum 초기화
    cnt = 2 # cnt 초기화
    flag = False 
    while True:
        sum = int(qu) * cnt # n의 배수로 곱하기
        sum_list = sorted(list(str(sum))) # n의 배수로 곱한값을 정렬해서 리스트에 저장        
        if len(qu_list) < len(sum_list): # 입력값보다 자릿수가 많아지면 break                   
            break            
        if qu_list == sum_list: # 입력값 리스트와 n의 배수로 곱한값 리스트의 숫자가 같으면 flag = True 하고 break
            flag = True
            break
        cnt += 1 # n의 배수로 곱하기 (1씩 증가한다)
    if flag: # flag = True면 possible, flag = False면 impossible 
        answer = 'possible'
    else:
        answer = 'impossible'
    print(f'#{tc} {answer}')
