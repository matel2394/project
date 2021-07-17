def solution(floors):
    counter = 0
    for i in range(len(floors)-1):
        if floors[i] < floors[i+1]:
            counter += floors[i + 1] - floors[i]
        if floors[i + 1] < floors[i]:
            counter += floors[i] - floors[i +1]
    return counter

floors = [1,2,5,4,2]
print(solution(floors))