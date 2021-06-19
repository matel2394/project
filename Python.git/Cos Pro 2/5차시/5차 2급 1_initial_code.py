def solution(ladders, win):
    answer = 0
    player = [1, 2, 3, 4, 5, 6]
    for e in ladders:
        temp = player[e[0]-1] #첫번째 사다리 temp 저장
        player[e[0]-1]=player[e[1]-1] #
        player[e[1]-1]= temp
    answer = player[win-1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]]
win = 3
ret = solution(ladders, win)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전:  File "D:\project\Python.git\Cos Pro 2\5차시\5차 2급 1_initial_code.py", line 6
         #@@@ = @@@
