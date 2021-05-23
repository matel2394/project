#문제2
def solution(price,grade):#함수
    answer = 0
    #지문 보고 코드 작성하는 곳
    if grade == "S":
        answer=  price * 0.95 # 1:100% 0.5 : 50% 0.25 : 25%
    if grade == "G":
        answer=  price * 0.9 # 1:100% 0.5 : 50% 0.25 : 25%
    if grade == "V":
        answer = price * 0.85  # 1:100% 0.5 : 50% 0.25 : 25%

    return answer

price1 = 2500
grade1 = "V"
ret1 = solution(price1,grade1) #함수 호출

print("solution return value of the function is",ret1,".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2,grade2) #함수 호출

print("solution return value of the function is",ret2,".")


