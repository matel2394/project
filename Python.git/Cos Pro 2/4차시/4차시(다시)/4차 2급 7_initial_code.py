def func_a(scores1, scores2): #점수 오른거 구하는 함수
    answer = 0
    for score1, score2 in zip(scores1, scores2): #(20,10),(50,50),(40,70)
        answer = max(answer, score2 - score1) #answer = 0, 0,30
    return answer #30 리턴

def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2): #(20,10),(50,50),(40,70)
        answer = min(answer, score2 - score1) # 수정 전:-10,0,-30 수정 후: -10,0,30
    return answer #-10 리턴
            
def solution(mid_scores, final_scores): # ab 호출해서 가장 많이떨군,올린 점수 구하기
    up = func_a(mid_scores, final_scores)
    down = func_b(mid_scores, final_scores)
    answer = [up, down]
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")