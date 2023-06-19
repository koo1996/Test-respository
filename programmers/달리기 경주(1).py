def solution(players, callings):
    b = {i : player for i,player in enumerate(players)}
    a = {player : i for i,player in enumerate(players)}
    for j in callings:
        loc1 = a[j]
        loc2 = a[j] - 1

        c = b[loc2]
        b[loc1] = c
        b[loc2] = j

        a[j] = loc2
        a[c] = loc1
    return list(b.values())