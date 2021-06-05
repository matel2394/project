def solution(characters):
    results = ""
    results += characters[0] #첫문자 문자를 results 저장
    for i in range(1,len(characters)): #하나씩비교
                #0[첫번째] 제외한 1번부터 비교
        if characters[i-1] != characters[i]:
            results += characters[i]
                #첫문자를 또 저장하면 오류
    return results

characters = "senteeeeeeeencccccccccccccccceeeeeeeeeeeeeeeeeee"
ret = solution(characters)
print("solution 함수결과",ret)