def func_a(passed, non_passed):#통과한 종목이 몇개인지 세는 함수
    return ( passed > 1 and non_passed ==0 )

def func_b(scores): #통과 점수의 반을 넘기지 못한 종목이 몇개인지 세는 함수
    answer = 0 #몇개인지 카운트 변수
    if scores[0] < 40: #만약 첫번째 항목이 절반을 넘지 못했다면
        answer += 1 #카운트에 1 더하기
    if scores[1] < 44: #만약 두번째 항목이 절반을 넘지 못 했다면
        answer += 1 #카운트에 1더하기
    if scores[2] < 35: #만약 세번째 항목이 절반을 넘지 못했다면
        answer += 1 #카운트에 1더하기
    return answer #카운트 리턴하기

def func_c(scores): #종목의 점수를 넘은 갯수 세는 함수
    answer = 0 #카운트 변수
    if scores[0] >= 80: #만약 스코어의 0번째가 80점보다 크거나 같으면
        answer += 1#카운트에 1 더하기
    if scores[1] >= 88:#만약 스코어의 0번째가 80점보다 크거나 같으면
        answer += 1#카운트에 1 더하기
    if scores[2] >= 70:#만약 스코어의 0번째가 80점보다 크거나 같으면
        answer += 1#카운트에 1 더하기
    return answer #카운트 리턴시키기

def solution(scores): #시험에 합격한 인원 수 구하는 함수
    answer = 0 #인원 카운트
    for my_score in scores: #스코어 리스트를 MY SCORE에 대입하며 반복
        passed = func_c(my_score) #통과여부는 C로 확인
        non_passed = func_b(my_score) #미통과 여부는 B로 확인
        answer += func_a(passed,non_passed) #인원 카운트에 A로 인원을 확인해 그 수만큼 추가
    return answer #카운트 반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

#수정 전 :  File "D:\project\Python.git\Cos Pro 2\4차시\4차 2급 2_initial_code.py", line 27
#     passed = func_@@@(@@@)
#                    ^
# SyntaxError: invalid syntax

#수정 후 : solution 함수의 반환 값은 1 입니다.
#       solution 함수의 반환 값은 4 입니다.

#문제에서 원하는 내용: 시험에 합격한 인원 수 구하기