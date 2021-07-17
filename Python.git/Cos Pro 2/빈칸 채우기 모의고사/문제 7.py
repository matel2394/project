def solution(schedule):
    answer = []
    for x,i in enumerate(schedule):
        if i == "X":
            answer.append(x+1)
    return answer
schedule = ["O","X","X","O","O","O","X","O","X","X"]
print(solution(schedule))