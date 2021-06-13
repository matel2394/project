def func_a(scores, score): #파라미터를 밑에있는 socres,n으로 사용함
    rank = 1 # 순위 #rank 변수에 1 대입
    for s in scores: #3번 반복
        if s == score: #만약 s가 n과 같다면
            return rank #rank를 리턴함
        rank += 1 #rank에 1을 추가함
    return 0 #0을 리턴함

def func_b(arr): #파라미터를 arr(scores)로 사용
    arr.sort(reverse=True) #socres 리스트를 내림차순 정렬해주는 함수

def func_c(arr, n): #파라미터를 arr(scores)와 n을 사용
    return arr[n] #scores의 n번째 수를 리턴함

def solution(scores, n): #scores와 n울 파라미터로 사용하는 함수
    score = func_c(scores,n) #스코어 변수에 scores의 3번째 수를 리턴하는 func_c함수를 scores와 n 파라미터로 호출해 대입함
    func_b(scores) #파라미터를 scores로 하는 func_b 함수 호출
    answer = func_a(scores,score) #answer변수에 func_a를 대입함
    return answer #func_a 함수가 들어간 answer 함수 리턴(func_a함수 호출)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3 #n 변수에 3 대입
ret = solution(scores, n) #solution 함수를 ret 변수에 대입

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.") #ret을 출력

#넣기 전:오류가 발생
#넣은 후: 정답인 3 나옴

#문제에서 원하는 내용: n번학생의 등수를 리턴해 출력하는 코드를 원함
