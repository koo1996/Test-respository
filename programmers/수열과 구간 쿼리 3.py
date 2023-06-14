def solution(arr, queries):
    for i in range(len(queries)):
        a = arr[queries[i][0]]
        b = arr[queries[i][1]]
        arr[queries[i][0]] = b
        arr[queries[i][1]] = a
    return arr

def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr