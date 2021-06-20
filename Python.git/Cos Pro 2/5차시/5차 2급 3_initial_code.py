def solution(speed, cars): #총 벌금 구하는 함수
    answer = 0 #총 벌금 카운트
    for x in cars: #cars 리스트의 값을 x에 대입
        if x >= speed * 11 / 10 and x < speed * 12 / 10: #규정 속도가 10%이상이고 20%미만이면
            answer += 3 #3만원 추가
        elif x >= speed * 12 / 10and x < speed * 13 / 10:#규정 속도가 20%이상이고 30%미만이면
            answer += 5#3만원 추가
        elif x >= speed * 13/ 10:#규정 속도가 30% 이상 위반이면
            answer += 7#3만원 추가
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")