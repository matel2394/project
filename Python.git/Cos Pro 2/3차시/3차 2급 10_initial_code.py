def solution(arr): #arr 리스트를 파라미터로 가진 함수
    answer = 0 #answer 변수에 0 대입
    for i in arr: #i에 arr의 내용물 넣으면서 5회 반복
        if i/2 in arr: #i를 2로 나눈 내용물이 arr 리스트 안에 있다면
            answer += 1 #answer에 1 추가
    return answer #answer 리턴

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
arr = [4, 8, 3, 6, 7]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")