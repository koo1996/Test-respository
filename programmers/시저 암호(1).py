def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - 65 + n) % 26 + 65)
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - 97 + n) % 26 + 97)
    return "".join(s)