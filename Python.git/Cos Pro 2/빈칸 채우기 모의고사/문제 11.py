def solution(password):
    count1, count2, count3 = 0, 0, 0
    for i in password:
        if i >= 'A' and i <= 'Z':
            count1 += 1
        elif i >= 'a' and i <= 'z':
            count2 += 1
        elif i >= '0' and i <= '9':
            count3 += 1
    if count1 >= 1 and count2 >= 1 and count3 >= 1 :
        answer = True
    else:
        answer = False
    return answer






password1 = "helloworld"
print(solution(password1))
password2 = "Hello123"
print(solution(password2))