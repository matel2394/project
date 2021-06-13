#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(scores): #scores를 파라미터로 사용하는 solution 함수 디파일(최하,최상점 빼고 평균구하는 함수)
    scores.sort(reverse=True) #스코어 리스트를 내림차순으로 정렬
    i = len(scores) #i변수에 scores 갯수 대입 (10)
    del scores[i-1] # 스코어 리스트의 i번째 인덱스에서 -1 을 뺀 9번째 인덱스를 삭제함(최하점 삭제)
    del scores[0]  #스코어 리스트의 가장 높은 점수인 0번째 인덱스를 삭제함 (최고점 삭제)
    i = len(scores) #i 변수에 scores 갯수 대입 (8)
    k= sum(scores) #k 변수에 scores의 모든 항목 더하기
    a=k//i #a변수에 모든 항목을 더한걸 항목 갯수로 나누기 (평균 구하기)
    answer = int(a) #answer 변수에 a 변수를 정수로 바꿔 대입
    return answer #answer 리턴

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

#수정 전:???

#수정 후:solution 함수의 반환 값은 49 입니다.
#solution 함수의 반환 값은 1 입니다.

#문제에서 원하는 내용: 최(고,하)점을 제외한 나머지 점수들의 평균 구하기
