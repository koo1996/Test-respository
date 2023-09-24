* [TIL](https://github.com/koo1996/TIL) 전에 사용했던 저장소

* TIL 저장소 오류로 인해 새로운 저장소 생성

* 다양한 알고리즘 문제 풀이

* 빅오 표기법
```
O(1) > O(logN) > O(N) > O(NlogN) > O(N^2) > O(N^3) > O(2^n)
```

* 유용한 vs code 확장 프로그램
  * JavaScript (ES6) code snippets : 코드 블록 자동 완성
  * HTML snippets
  * ESLint : 자바스크립트 문법의 오류를 찾아주는 확장프로그램
  * Prettier - Code formatter
  * Live Server : HTML 파일을 바로 웹 서버에서 실행할 수 있도록 해주는 확장프로그램

시간제한이 1초인 문제를 만났을 때 일반적인 기준
N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)
N의 범위가 2000인 경우 : 시간 복잡도가 O(N^2)
N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)
N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)
```

``` python
import time
start_time = time.time() # 측정 시작
# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
1. 백트래킹
2. 스택
```

```python
stack.append(2)
stack.append(5)
stack.append(8)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
# In 2 - 5 - 8 / Out 8 - 5 - 2  
```
3. 큐, 덱
```python
# 큐
data.put(2)
data.put(5)
data.put(8)

#FIFO
print(data.get())
print(data.get())
print(data.get())
# 2 5 8
```
4. 이분 탐색
5. 우선순위 큐
6. 그래프와 순회
7. 투 포인터
8. 최단 경로

기본) 스택,큐,우선순위큐,Deque(★),해시맵,문자열

초급) PriorityQueue 완전탐색

중급) BinarySearch DFS BFS Recursion

심화) Graph DP

알고리즘 사이트 
1. 백준 : https://www.acmicpc.net/

2. sw expert academy(삼성) : https://swexpertacademy.com/main/main.do

3. 프로그래머스: https://programmers.co.kr/


* 파이썬과 큐(Queue)
  * Enqueue : 큐에서 데이터를 입력하는 기능

  * Dequeue : 큐에서 데이터를 꺼내는 기능
  
* 스택(Stack)
  * 나중에 넣은 데이터를 먼저 빼는 후입선출(LIFO - Last In First Out) 구조
  * ex) 박스 쌓기, 트럭에 물건 넣기
  * 파이썬 기본 리스트에서 append()와 pop() 메서드를 사용하여 구현

---------------------------

* JavaScript - [JS](JavaScript/)

* Java - [Java](Java/)

