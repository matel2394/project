def solution(attack,recovery,hp):
    answer = 0
    while hp>0:
        hp -= attack
        hp +=recovery
        answer += 1
    return answer

attack = 30
recovery = 10
hp = 60

print(solution(attack,recovery,hp))