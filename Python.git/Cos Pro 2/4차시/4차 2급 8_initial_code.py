def solution(n, votes): #과반수를 득표한 후보의 번호를 구하는 함수 #n은 후보자 수 #votes는 투표 리스트
    arr = [0] * (n + 1) #arr 리스트생성해서 0으로 전부 초기화
    for vote in votes: #투표리스트 하나씩 vote에 대입
        arr[vote] += 1 #arr[투표번호=vote] 1씩 증가

    for i in range(1, n+1): #1부터 n까지 1씩 증가
        if arr[i] > len(votes)/2: #투표리스트가 votes항목을 2로 나눈것보다 클때
            return i
    return -1

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
    #1번:4개
    #2번:2개
    #3번:2개
ret1 = solution(n1, votes1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
    #1번 3개
    #2번 4개
    #3번 0개
ret2 = solution(n2, votes2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")

#수정 전:solution 함수의 반환 값은  1  입니다.
#       solution 함수의 반환 값은  1  입니다.

#수정 후:

#문제에서 원하는 것:과반수를 득표한 후보의 번호 구하기