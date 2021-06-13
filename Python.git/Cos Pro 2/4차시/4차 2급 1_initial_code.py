def solution(schedule):
    answer = [] #상담 못받은 학생들 번호 리스트
    for idx, i in enumerate(schedule):
        if i == "X":
            answer.append(idx+1)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


#수정 전:  File "D:\project\Python.git\Cos Pro 2\4차시\4차 2급 1_initial_code.py", line 4
#     if i == @@@:
#             ^
# SyntaxError: invalid syntax

#수정 후:

#문제에서 원하는 내용 :상담을 받지 못한 학생들의 번호를 오름차순 정리