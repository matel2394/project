def solution(attack,recovery,hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    return count

attack = 30
recovery = 10
hp = 60
ret = solution(attack,recovery,hp)

print(ret)

#몬스터 60
#count = 1  #공격 -30 => 몬스터30
            #회복 +10 => 몬스터40

# count = 2 #공격 -30 => 몬스터10
            # 회복 +10 => 몬스터20

# count = 3 #공격 -30 => 몬스터 -10
            # 회복 +10 => 몬스터 0

