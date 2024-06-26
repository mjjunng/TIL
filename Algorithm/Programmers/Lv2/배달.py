from collections import deque

def solution(N, road, K):
    answer = 0
    q = deque()
    graph = [[] for _ in range(N+1)]
    dis = [float('inf') for _ in range(N+1)]
    dis[1] = 0
    
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    q.append(1)
    
    while q:
        node = q.popleft()
        
        for b, c in graph[node]:
            if dis[node] + c < dis[b]:
                dis[b] = dis[node] + c
                q.append(b)
    
    for i in range(1, len(dis)):
        if dis[i] <= K:
            answer += 1
                
    return answer


## 다익스트라
import heapq

def solution(N, road, K):
    answer = 0
    hq = []
    graph = [[] for _ in range(N+1)]
    dis = [float('inf') for _ in range(N+1)]
    dis[1] = 0
    
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    heapq.heappush(hq, [0, 1])
    
    while hq:
        v, node = heapq.heappop(hq)
        
        for b, c in graph[node]:
            if dis[node] + c < dis[b]:
                dis[b] = dis[node] + c
                heapq.heappush(hq, [dis[b], b])
    
    for i in range(1, len(dis)):
        if dis[i] <= K:
            answer += 1
                
    return answer
