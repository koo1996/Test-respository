def solution(board, moves):
    answer = 0
    save_ = []
    stack = []
    for k in moves: #인형뽑기 
        for i in range(len(board)):
            if board[i][k-1] != 0:
                save_.append(board[i][k-1])
                board[i][k-1] = 0
                break

    for j in save_: #같은 모양의 인형 삭제
        if not stack:
            stack.append(j)
        else:
            if stack[-1] == j:
                stack.pop(-1)
                answer += 2
            else:
                stack.append(j)               
    return answer