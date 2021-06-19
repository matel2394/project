# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(scores, cutline):#scores는 점수리스트 cutline은 점수컷
    answer = 0 #합격자 수
    for i in scores: #i에 scores 대입하며 반복
        if i >= cutline: #만약 i가 커트라인보다 크거나 같으면
            answer += 1 #합격자수 1 증가
    return answer #리턴

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")