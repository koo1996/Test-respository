def solution(number):
    sum = 0
    for i in number:
        sum += int(i)
    if int(number) % 9 == sum % 9:
        return sum % 9