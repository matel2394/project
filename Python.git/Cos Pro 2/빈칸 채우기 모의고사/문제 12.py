def solution(money, chairs, desks):
    answer = 0
    for chair in chairs:
        for desk in desks:
            price = chair + desk
            if answer <= price and price <= money:
                answer = price
    return answer




money1 = 7
chairs1 = [2,5]
desks1 = [4,3,5]
print(solution(money1,chairs1,desks1))
money2 = 7
chairs2 = [3]
desks2 = [5]
print(solution(money2,chairs2,desks2))
