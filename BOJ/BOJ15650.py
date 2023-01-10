n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)

#백트래킹 구현
#해를 구하는 도중 해가 아니어서 막히면 막히기 전으로 다시 돌아가서 해를 찾는 기법
#가상의 트리에서 해를 구하기 위해 부모 노드에서 자식 노드까지 뻗어나간다. 만약 해당 노드가 조건에 맞지 않는다면 다시 부모노드로 돌아간다.
#해가 아닌 선택지는 없애면서 탐색하기 때문에 시간복잡도를 줄일 수 있다.