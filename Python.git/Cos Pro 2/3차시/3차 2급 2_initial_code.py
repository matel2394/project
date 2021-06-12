def func_a(current_grade, last_grade, rank, max_diff_grade): #파라미터를 밑의 두 리스트와 solution 함수 안에있는 rank,max_diff_grade를 사용하는 함수
    arr_length = len(current_grade) #arr_length 변수에 current grade의 내용 수를 대입
    count = 0 #카운트 변수에 0 대입
    for i in range(arr_length): #i에 1씩 더하며 6회 반복
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10: #current grade의 i 값이 80보다 큰지,
            count += 1 #그렇다면 count 변수에 1 더하기
        elif current_grade[i] >= 80 and rank[i] == 1: #current grade의 i 값이 80보다 큰지,
            count += 1 #그렇다면 count 변수에 1 더하기
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            # max_diff_grade가 0보다 크고 current grade의 i 번째에서 last grade의 i값을 뺀것과 같다면
            count += 1 #그렇다면 count 변수에 1 더하기
    return count #count 변수를 리턴시킴

def func_b(current_grade): #current grade 리스트를 파라미터로 쓰는 func_b 함수
    arr_length = len(current_grade) #arr_length 변수에 current grade의 내용 수를 대입
    rank = [1] * arr_length #rank는 1이 들어가있는 리스트고 거기에 arr_length(6)을 곱함
    for i in range(arr_length): #i에 1씩 더하며 6회 반복
        for j in range(arr_length):#j에 1씩 더하며 6회 반복
            if current_grade[i] < current_grade[j]: #만약 current grade의 i번째 인덱스가 currunt grade의 j번째 인덱스보다 작으면
                rank[i] += 1 #rank의 i번째 인덱스에 1 더하기
    return rank #rank 리스트 리턴하기

def func_c(current_grade, last_grade): #파라미터를 밑의 두 리스트를 사용하는 함수
    max_diff_grade = 1 #max diff grade 변수에 1 대입
    for i in range(len(current_grade)): #6회 반복
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
        # max diff grade 변수에 max diff grade와,current grade의 i번째 인덱스 - last grade의 i번째 인덱스의 경우의 수중 가장 큰 수를 max diff grade에 대입
    return max_diff_grade #max diff grade를 리턴

def solution(current_grade, last_grade): #밑의 두 리스트를 파라미터로 사용하는 solution이름의 함수
    rank = func_b(current_grade) #rank 변수에 current grade를 파라미터로 쓰는 func_b함수 대입
    max_diff_grade = func_c(current_grade,last_grade) #max diff grade 변수에 current grade와 last grade를 파라미터로 쓰는 func_c함수 대입
    answer = func_a(current_grade,last_grade,rank,max_diff_grade)
    #answer 함수에 max diff grade 변수에 current grade와 last grade,rank,max diff grade를 파라미터로 쓰는 func_a함수 대입
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전:   File "C:/Users/User/Documents/python/project/Python.git/Cos Pro 2/3차시/3차 2급 2_initial_code.py", line 29
#     rank = func_@@@(@@@)
#                  ^
# SyntaxError: invalid syntax

#수정 후 :solution 함수의 반환 값은 3 입니다.

#문제에서 원하는 내용:학교에서 장학금을 받을수있는 조건을 맞춘 학생을 구하는것