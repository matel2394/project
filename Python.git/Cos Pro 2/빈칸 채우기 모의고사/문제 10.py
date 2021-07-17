def solution(taekwondo,running,shooting):
    count = 0
    count2 =0
    if taekwondo >= 25:
        count += 250
    else:
        count += 8 * taekwondo
    if running ==60 :
        count += 250
    elif running <= 60:
        count += 250 + ((running - 60) * 5)
    elif running >= 60:
        count += 250 - ((running - 60) * 5)
    for i in shooting:
        if i == 10:
            count2 += 1
            if count2 >= 7:
                count += 100
    count += sum(shooting)
    return count

taekwondo = 27
running =63
shooting = [9,10,8,10,10,10,7,10,10,10]

print(solution(taekwondo,running,shooting))