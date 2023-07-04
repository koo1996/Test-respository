def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            score[0] += 1
        if answers[i] == student2[i%len(student2)]:
            score[1] += 1
        if answers[i] == student3[i%len(student3)]:
            score[2] += 1

    for j in range(len(score)):
        if score[j] == max(score):
            answer.append(j+1)


    return answer