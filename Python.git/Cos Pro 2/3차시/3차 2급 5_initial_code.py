def solution(member_age, transportation): #member age와 transportation을 파라미터로 하는 sloution 함수 디파일 (타고가는 수단에 따른 요금과 총 요금 구하는 함수)
	if transportation == 'Bus': #만약 transportation이 버스라면
		adult_expense = 40000 #어른요금 40000
		child_expense = 15000 #아이요금 15000
	elif transportation == 'Ship': #만약 transportation이 배라면
		adult_expense = 30000 #어른요금 30000
		child_expense = 13000 #아이요금 15000
	elif transportation == 'Airplane': #만약 transportation이 비행기라면
		adult_expense = 70000 #어른요금 70000
		child_expense = 45000 #아이요금 45000

	if len(member_age) >= 10: #인원 구하기
		adult_expense = adult_expense * 90/100 #어른요금에 0.9 곱하기 (할인 받으면 얼만지 구하기)
		child_expense = child_expense * 80/100 #아이요금에 0.9 곱하기 (할인 받으면 얼만지 구하기)

	total_expenses = 0 #total_expenses 변수에 0 대입 (최종 합계 가격 변수)
	for age in member_age: #age 변수에 member_age 의 항목을 대입하며 반복
		if age>=20: #만약 age 변수가 20보다 크거나 같다면 (나이에 따른 어른,어린이 구하기)
			total_expenses += adult_expense # total 가격에 어른요금만큼 더하기
		else: #아니면
			total_expenses += child_expense #아이 요금만큼 더하기

	return total_expenses #토탈가격 리턴


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

#수정 전 : ???

#수정 후:solution 함수의 반환 값은 150000 입니다.
#solution 함수의 반환 값은 203600.0 입니다.

#문제에서 원하는 내용: 인원의 수와 나이에 따른 총 가격 구하기