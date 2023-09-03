def solution(myString):
    for i in range(len(myString)):
        if myString[i] == 'a':
            replace('a','A')
        else:  
            myString.upper()
        
    return myString