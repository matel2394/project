#151번
print("151번")
리스트1 = [3,-20,-3,44]
for 변수 in 리스트1:
    if 변수 < 0:
        print(변수)
#152번
print("152번")
리스트2 = [3,100,23,44]
for 변수 in 리스트2:
    if 변수 % 3 == 0:
        print(변수)
#153번
print("153번")
리스트3 = [13,21,12,14,30,18]
for 변수 in 리스트3:
    if 변수 % 3 == 0 and 변수<=20:
        print(변수)
#154번
print("154번")
리스트4 = ["I","study","python","language","!"]
for 변수 in 리스트4:
    if len(변수) >= 3 :
        print(변수)
#155번
print("155번")
리스트5 = ["A","b","c","D"]
for 변수 in 리스트5:
    if 변수.isupper() == True:
        print(변수)
#156번
print("156번")
리스트5 = ["A","b","c","D"]
for 변수 in 리스트5:
    if 변수.isupper() == False:
        print(변수)
#157번
print("157번")
리스트6 = ['dog','cat','parrot']
for 변수 in 리스트6:
    print(변수.title())
#158번
print("158번")
리스트7 = ['hello.py','ex01.py','intro.hwp']
for 변수 in 리스트7:
    변수1 = 변수.split('.')
    print(변수1[0])
#159번
print("159번")
리스트8 = ['intra.h','intra.c','define.h','run.py']
for 변수 in 리스트8:
    변수1 = 변수.split('.')
    if 변수1[1] == 'h':
        print(변수)
#160번
print("160번")
리스트8 = ['intra.h','intra.c','define.h','run.py']
for 변수 in 리스트8:
    변수1 = 변수.split('.')
    if 변수1[1] == 'h' or 변수1[1] == 'c':
        print(변수)