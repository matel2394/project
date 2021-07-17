def solution(member,trasportation):
    counter = 0
    if trasportation == "bus":
        for i in member:
            if len(member) >= 10:
                if i < 20:
                    counter += 15000 * 80 // 100
                elif i >= 20:
                    counter += 40000 * 90 // 100
            else:
                if i < 20:
                    counter += 15000
                elif i >= 20:
                    counter += 40000

    if trasportation == "ship":
        for i in member:
            if len(member) >= 10:
                if i < 20:
                   counter += 13000 * 80//100
                elif i >= 20:
                    counter += 30000 * 90//100
            else:
                if i < 20:
                    counter += 13000
                elif i >= 20:
                    counter += 30000
    if trasportation == "airplane":
        for i in member:
            if len(member) >= 10:
                if i < 20:
                   counter += 45000 * 80//100
                elif i >= 20:
                    counter += 70000 * 90//100
            else:
                if i < 20:
                    counter += 45000
                elif i >= 20:
                    counter += 70000
    return counter








member_age1 = [13,33,45,11,20]
transportation1 ="bus"
print(solution(member_age1,transportation1))
member_age2 = [25,11,27,56,7,19,52,31,77,8]
transportation2 = "ship"
print(solution(member_age2,transportation2))