def solution(my_string, queries):
    answer = ''
    for i,j in queries:
        answer = my_string[i:j+1]
        reverse_answer = answer[::-1]
        my_string = my_string[:i] + reverse_answer + my_string[j+1:]
    return my_string