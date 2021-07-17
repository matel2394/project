def solution(cars,speed):
    answer = 0
    for i in cars:
        if i >= speed * 110//100 and i < speed * 120//100:
            answer += 3
        elif i >= speed * 120//100 and i < speed * 130//100:
            answer += 5
        elif i >= speed * 130//100:
            answer += 7
    return answer


cars = [110,98,125,148,120,112,89]
speed = 100

print(solution(cars,speed))