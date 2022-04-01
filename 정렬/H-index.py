def solution(citations):
    h = 0
    
    while len([x for x in citations if x >= h]) >= h:
        h += 1

    answer = h -1
    
    return answer