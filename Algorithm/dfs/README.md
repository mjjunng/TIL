# DFS과 BFS

### DFS vs BFS

### DFS

- 완전탐색: 어떻게든 전체 탐색을 할 수 있도록 가지를 뻗어야 함
- *상태 트리
- 종료 조건 확실히 파악해야 함
- 최대 점수/가지수 문제

### BFS

- 최단 거리 문제

## 👉 상태트리

![이미지 3](https://user-images.githubusercontent.com/52596617/210076145-5f4e8a52-bc07-4c88-9721-16ba25324c99.png)

## DFS?

시작 노드부터 최대한 깊이 파고 들어가면서 그래프를 탐색하는 방법이다.

### 원리

DFS는 **스택**을 사용하는 원리와 같다. 

시작 노드를 스택에 넣고, 넣은 노드를 스택에서 꺼낸다. 꺼낸 노드의 모든 자식 노드를 스택에 넣는다(단, 이전에 한 번이라도 스택에 넣었던 노드는 다시 스택에 넣지 않는다). 이전에 꺼낸 노드를 출력한다. 

이 과정을 스택이 빌 때 까지 반복한다. 

### 공식

```python
def DFS(L, sum, ...):
	if 빠져나갈 조건 (대부분 L == n+1)
		if res < s:  # 최대값 or 최소값 문제인 경우 
			res = s
		return
	
	else:
		DFS(L+1, sum+lst[L])  # 노드 방문한 경우 
		DFS(L+1, sum)  # 노드 방문하지 않은 경우 

DFS(0, 0)
```

## BFS?

시작 노드부터 시작해서 인접한 노드를 우선적으로 넓게 탐색하는 방법이다. 

> 💡 두 노드의 **최단경로**를 찾을 때 많이 사용함
> 

### 원리

BFS는 DFS의 원리와 같지만, 큐를 사용한다. 

시작 노드를 큐에서 넣고, 노드를 큐에서 꺼낸다. 꺼낸 노드의 자식 노드를 큐에 넣는다(단, 이전에 한 번이라도 큐에 넣었던 노드는 다시 큐에 넣지 않는다). 이전에 꺼낸 노드를 출력한다. 

이 과정을 큐가 빌 때까지 반복한다.

### 공식

```python
// 방문 체크하는 리스트 거의 필요함 

dq.append(시작 노드)

while dq:
	now = dq.popleft()
	if 빠져나갈 조건 (대부분 now == 주어진 값):
		break
	
	for i in range(4): // 상하좌우 탐색 
		if i가 idx 안 벗어나는 지 체크:
			dq.append(i)
```

### 그래프 표현 방법

### 1. 인접 행렬

2차원 배열로 그래프의 연결 관계 표현

### 2. 인접 리스트

리스트로 그래프의 연결 관계 표현 

[[(노드, 거리)], [(노드, 거리)]]
