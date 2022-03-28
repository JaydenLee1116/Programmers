def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        if i != j:
            temp = sorted(array[i-1:j])[k-1]            
            answer.append(temp)
        else:
            temp = array[i-1]
            answer.append(temp)
    return answer