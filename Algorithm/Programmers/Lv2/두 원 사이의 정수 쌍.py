import math

def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2+1):
        max_y = int((r2 ** 2 - x ** 2) ** 0.5)
        min_y = 0
        
        if x < r1:
            min_y = math.ceil((r1 ** 2 - x ** 2) ** 0.5)
        
        answer += max_y - min_y + 1
            
    return answer * 4
