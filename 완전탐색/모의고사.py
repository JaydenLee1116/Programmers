def solution(answers):
    length = len(answers)
    unit1 = [1, 2, 3, 4, 5]
    unit2 = [2, 1, 2, 3, 2, 4, 2, 5]
    unit3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    arr1 = unit1 * (length // 5) + unit1[:length % 5 + 1]
    arr2 = unit2 * (length // 8) + unit2[:length % 8 + 1]
    arr3 = unit3 * (length // 10) + unit3[:length % 10 + 1]
    
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(length):
        if answers[i] == arr1[i]:
            count1 += 1
        if answers[i] == arr2[i]:
            count2 += 1
        if answers[i] == arr3[i]:
            count3 += 1
    
    answer = []
    max_count = max(count1, count2, count3)
    
    
    if count1 == max_count:
        answer.append(1)
    if count2 == max_count:
        answer.append(2)
    if count3 == max_count:
        answer.append(3)
        
    return answer