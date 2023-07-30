def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack: #stack이 비어있다면 s[i] 추가
            stack.append(s[i])
        else: #stack이 마지막 자리에 '(' 가 있고 s[i]에 ')'가 있다면 소거시킨다. 
            if stack[-1] == '(':
                if s[i] == ')':
                    stack.pop(-1)
                else:
                    stack.append(s[i]) #'(' '('
            else:
                return False #stack[-1]이 ')'라면 오답이다.      
    if stack: #for문이 끝난 시점에 stack이 비어있지 않으면 오답이다.
        return False

    return True