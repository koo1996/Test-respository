def solution(s, skip, index):
    answer = ''
    alphabet_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        if i in alphabet_:
            alphabet_.remove(i)
    for i in s:
        pos = (alphabet_.index(i) + index) % len(alphabet_)
        answer += alphabet_[pos]
    return answer