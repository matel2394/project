def solution(calorie):
    min_cal = calorie[0] # 713,665,873,500,751
    answer = 0
    for cal in calorie: # cal = 713,665,873,500,751
        if cal > min_cal: # 713 > 713, 665>713 , 873 > 665 , 500>665, 751 > 500
            answer += cal - min_cal #208 #251 = 208 + 251 = 459
        min_cal = min(min_cal, cal) #min cal = 713,665
    return answer # 459

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")