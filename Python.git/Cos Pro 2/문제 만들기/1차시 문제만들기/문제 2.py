#문제 2


def solution(rank,price):
    count = 0
    for i in rank:
        if i == "S":
            count += price * 95//100
        if i == "G":
            count += price * 90//100
        if i == "V":
            count += price * 85//100
    return count

rank1 = "V"
price1 = 2500

ret1 = solution(rank1,price1)
print(ret1)

rank2 = "S"
price2 = 96900

ret2 = solution(rank2,price2)
print(ret2)




