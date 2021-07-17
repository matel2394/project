def solution(classes,m):
    count = 0
    for i in classes:
        count += i//m
        if i%m >0:
            count += 1
    return count

classes = [80,45,33,20]
m = 30

print(solution(classes,m))