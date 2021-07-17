#문제1
    #조건1 : 리스트에 사이즈별로 개수를 담아서 리턴해주는 함수
선호티셔츠 = ["S","S","XS","L","XXL","S","XL","L"]
    #XS = 1 S= 3 M = 0 L = 2 XL = 1 XXL = 1
    #[1,3,0,2,1,1]
def 함수(list):
    count = [0 for _ in range(6)] #갯수 세는 리스트 하나 만들어서 사이즈 갯수만큼 0 만들어줌
    for i in list:
        if i == "XS":
            count[0] += 1
        if i == "S":
            count[1] += 1
        if i == "M":
            count[2] += 1
        if i == "L":
            count[3] += 1
        if i == "XL":
            count[4] += 1
        if i == "XXL":
            count[5] += 1

    return count#함수 반환

ret = 함수(선호티셔츠)
print(ret)


##############################################################################################################

#학생들 학년별 인원 세기
age = [8,8,9,10,10,10,11,9,8,12,13,8,11]

def solution(age):
    answer = [0 for _ in range(6)]
    for i in age:
        if i == 8:
            answer[0] += 1
        if i == 9:
            answer[1] += 1
        if i == 10:
            answer[2] += 1
        if i == 11:
            answer[3] += 1
        if i == 12:
            answer[4] += 1
        if i == 13:
            answer[5] += 1
    return answer

ret2 = solution(age)
print(ret2)

################################################################################################################
drink = []