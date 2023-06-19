cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
answer = 0
for i in range(len(goal)):
    if len(cards1) > 0:
        if cards1[0] == goal[i]:
            cards1.pop(0)  
    elif len(cards2) > 0:         
        if cards2[0] == goal[i]:
            cards2.pop(0)
    else:
        answer = 0

if len(cards1) == 0 and len(cards2) == 0:
    print(1)
else:
    print(2)

def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) == 0:
            break
        else:
            if cards1[0] == i:
                cards1.pop(0)  
    
        if len(cards2) == 0:
            break
        else:         
            if cards2[0] == i:
                cards2.pop(0)
    if len(cards1) == 0 and len(cards2) == 0:
        return "Yes"
    else:
        return "No"