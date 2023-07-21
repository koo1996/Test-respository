def solution(id_list, report, k):
    report = list(set(report)) #중복 신고 방지

    id_a = {i:0 for i in id_list} #처리 결과 메일 받은 횟수
    id_b = {i:0 for i in id_list} #신고 받은 횟수
    for i in range(len(report)): #신고 받은 사람은 value 1씩 증가
        report[i] = report[i].split(' ')
        id_b[report[i][1]] = id_b.get(report[i][1],0) + 1

    for j in range(len(report)): #신고 받은 사람 value가 k보다 크거나 같으면 신고 한 사람이 value는 1씩 증가
        if id_b[report[j][1]] >= k:
            id_a[report[j][0]] = id_a.get(report[j][0],0) + 1


    return list(id_a.values())