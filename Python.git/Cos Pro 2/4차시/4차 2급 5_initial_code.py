def solution(calorie): #운동으로 소모하는 열량을 구하는 함수
    min_cal = calorie[0] #전날대비 적은 칼로리 변수
    answer = 0 #총 열량 변수
    for cal in calorie: #변수에 칼로리 리스트 넣으며 반복
        if cal > min_cal: #만약 변수가 적은 칼로리변수보다 크면
            answer += cal - min_cal #거기서 적은 칼로리를 빼고 총 열량에 더함
        min_cal = min(min_cal, cal) #그리고 둘중에 더 작은 수를 min cal에 넣음
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전 : solution 함수의 반환 값은 3502 입니다.

#수정 후 :solution 함수의 반환 값은 459 입니다.

#문제에서 원하는 내용 : 운동으로 소모하는 총 열량 구하기