def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == "1" and mode == 0:
            mode = 1
        elif code[i] == "1" and mode ==1:
            mode = 0
        elif i % 2 == 0 and mode == 0:
            answer += code[i]
        elif i % 2 == 1 and mode == 1:
            answer += code[i]

    return answer if answer else "EMPTY"

# def solution(code):
#     return "".join(code.split("1"))[::2] or "EMPTY"