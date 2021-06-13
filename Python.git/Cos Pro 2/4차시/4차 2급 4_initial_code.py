def solution(classes, m): #필요한 조교 수를 구하는 함수
    answer = 0 #조교 수 카운트
    for students in classes: #변수에 클래스 리스트의 항목을 넣으며 반복함
        answer += students // m #80,45,33,20등을 조교 1인당 담당학생 수 으로 나눈 몫만을 조교 수 카운트에 더함
        if students % m != 0: #만약 변수를 담당학생 수로 나눈게 0이 아니라면
            answer += 1 #조교 1명 더하기
    return answer #리턴

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전:   File "D:\project\Python.git\Cos Pro 2\4차시\4차 2급 4_initial_code.py", line 4
#     answer += students @@@ m
#                         ^
# SyntaxError: invalid syntax

#수정 후: solution 함수의 반환 값은 8 입니다.

#문제에서 구하고자 하는 내용:수업을 진행하기 위한 조교 수 구하기