def solution(taekwondo, running, shooting): #총 점수를 구하는 함수
    answer = 0 #총 점수 카운트
    if taekwondo >= 25: #패배 조건은 생각하지 않고 종목이름을 승리로 한다면 25승 이상일때
    	answer += 250 #총 점수 카운트에 250점을 더함
    else: #아니면
    	answer += taekwondo * 8 #1승당 8점이니까 카운트에 승 수*8을 더해준다
    answer += 250 + (60 - running) * 5 #이 구문은 달리기 구문으로 기본점수 250점에다가 (이 구문에서 초는 running이다) 60에서 걸린 시간을 빼고 5를 곱한것을 더한다
    count = 0
    for s in shooting: #슈팅 리스트값을 대입하며 반복
    	answer += s #총 점수 카운트에 모든 점수를 더해주고
    	if s == 10: #만약 리스트의 값중 10이 있으면
    		count += 1 #1씩 더해주기
    if count >= 7: #만약 위에서 10으로 1씩 더한값이 7점 이상이면
    	answer += 100 #추가점수 100점 주기
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 후:solution 함수의 반환 값은 679 입니다.

#문제에서 원하는 내용: 위 세 종목의 총 점수 합계