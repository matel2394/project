def func_a(time_table): #마지막 수업시간 구하는 함수
    answer = 0
    for i, t in reversed(list(enumerate(time_table))): #reversed : 반대
        #i는 인덱스 t는 리스트 요소
        #뒤집어서
        if t == 1: #if 만약 문에 t를 계속 넣어보며 그 요소가 1이라면
            answer = i #t에 맞는 i의 인덱스를 answer로 정하고 브레이크
            break
    return answer

def func_b(time_table, class1, class2): #시간표,첫수업,마지막 수업이 인수
    answer = 0 #공강 시간 카운트
    for i in range(class1, class2): # time table 리스트 기준 0부터 6까지 반복
        if time_table[i] == 0: #만약 time table의 i번째 인덱스 요소가 0이면
            answer += 1 #공강시간 카운트에 1 추가
    return answer

def func_c(time_table): #첫 수업 시작시간 수하는 함수
    answer = 0
    for i, t in enumerate(time_table):
        # i는 인덱스 t는 리스트 요소
        if t == 1:#if 만약 문에 t를 계속 넣어보며 그 요소가 1이라면
            answer = i#t에 맞는 i의 인덱스를 answer로 정하고 브레이크
            break
    return answer

def solution(time_table): #공강 시간 구하는 함수
    answer = 0
    first_class = func_c(time_table) #첫 수업 시작시간
    last_class = func_a(time_table) #마지막 수업 시작시간
    answer = func_b(time_table,first_class,last_class) #1과 2 사이의 수업 없는시간 구하기
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0] #시간표
                #1 수업
                #0 공강
ret = solution(time_table)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 후:solution 함수의 반환 값은 3 입니다.

#문제에서 원하는 내용:공강은 총 몇시간인가

