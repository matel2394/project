def func_a(scores1, scores2): #성적 가장 많이 오른 학생 점수 차이 구하는 함수
    answer = 0 #오른 점수 저장변수
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1) #저장변수에 answer과 기말에서 중간성적을 빼서 더 큰걸 저장
    return answer #변수 리턴

def func_b(scores1, scores2):#성적 가장 많이 떨어진 학생 점수 차이 구하는 함수
    answer = 0 #떨어진 점수 저장변수
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score2 - score1 )#저장변수에 answer과 기말에서 중간성적을 빼서 더 작은걸 저장
    return answer #변수 리턴
            
def solution(mid_scores, final_scores): #성적이 가장 많이 오른 학생과 가장 떨어진 학생의 기말과 중간 성적차이 저장하는 함수
    up = func_a(mid_scores, final_scores) #up변수에 오른학생 점수 저장
    down = func_b(mid_scores, final_scores) #down 변수에 떨어진 학생 점수 저장
    answer = [up, down] #answer에 up,down 리스트 저장
    return answer #리턴

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#수정 전 :solution 함수의 반환 값은 [30, -30] 입니다.
#수정 후 :
#문제에서 구하려고 하는 것:성적이 가장 많이 오른 학생과 가장 떨어진 학생의 기말과 중간 성적차이