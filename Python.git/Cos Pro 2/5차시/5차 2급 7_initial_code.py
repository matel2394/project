def solution(stuffs): #물건수가 인수 (모든 물건을 계산하는데 걸리는 시간 구하는 함수)
    answer = 0 #걸리는 시간 카운트
    small_counter, general_counter = 0, 0 #두 변수에 0 대입
    for s in stuffs: #s에 stuffs 요소 대입 반복
        if s > 3: #만약 물건 수가 3개보다 많으면
            general_counter += s #일반 카운터에 물건 1개 계산시간이 1분이므로 물건 갯수만큼 더하기
        else: #아니면
            small_counter += s # 소량 카운터에 물건 갯수만큼 더하기
    if small_counter > general_counter: #만약 소량 카운터 변수가 일반보다 더 크면
        answer = small_counter #소량카운터가 총 걸린 시간
    else: #아니면
        answer = general_counter #일반계산대
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
stuffs = [5, 3, 4, 2, 3, 2]
ret = solution(stuffs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")