#문제 3
def func_a(month,day):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31] #각 월의 마지막날
    total = 0
    for i in range(month-1): #월 -1 만큼 반복하기
        total += month_list[i] #입력한 월의 전 월까지의 일수를 다 더하기
    total += day #내가 입력한 월의 일수 더하기
        #총 1월 1일부터 내가 입력한 날짜까지의 일수를 구하기
    return total - 1

def solution(start_month,start_day,end_month,end_day):
    start_total = func_a(start_month,start_day) #시작 날짜
    end_total = func_a(end_month,end_day) #끝 날짜
    return end_total - start_total #끝 날짜 - 시작 날짜

start_month = 1 #시작 날짜의 월
start_day =2 #시작 날짜의 일
end_month = 2 #끝 날짜의 월
end_day = 2 #끝 날짜의 일
ret = solution(start_month,start_day,end_month,end_day)
        #함수 불러내기
print("solution: return value of the function is",ret,".")

#start month의 func_a함수는 for문이 0회반복이라 month를 무시해주고 밑에있는 total+= day에 start day를 넣어주면 start total은
#1이 됨
#end month의 func a함수는 2-1이니 for문이 1회반복이고 i=0이 나오니까 토탈에 31이 더해져서 대입되고 밑에있는 total += day에는
#2가 더해져서 total = 33인데 return에 -1이 있으니 end total = 32
#솔루션 함수에서 end total - start total이니 31일
#매개변수 ret에 저장되고 마지막 print함수에 출력