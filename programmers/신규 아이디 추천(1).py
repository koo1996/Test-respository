def solution(new_id):

    check_ = ['-', '_', '.']
    new_id = new_id.lower() #1단계

    for i in new_id: #2단계
        if not i.isalpha() and not i.isdigit():
            if not i in check_:
                new_id = new_id.replace(i,'')

    while '..' in new_id: #3단계
        new_id = new_id.replace('..', '.')

    if new_id[0] == '.' and len(new_id) > 1: #4단계
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    if not new_id: #5단계
        new_id += "a"

    if len(new_id) >= 16: #6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 3: #7단계
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id