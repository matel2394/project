# #161번
# print("161번")
# for i in range(100):
#     print(i)
#162번
print("162번")
print(list(range(2002,2051,4)))
#163번
print("163번")
print(list(range(0,31,3)[1::]))
# #164번
# print("164번")
# for i in range(100)[::-1]:
#     print(i)
#165번
print("165번")
for 변수 in range(10):
    print(변수/10)
#166번
print("166번")
for 변수 in range(10)[1::]:
    print("3 x",변수,"=", 3*변수)
#167번
print("167번")
for 변수 in range(10)[1:10:2]:
    print("3 x",변수,"=", 3*변수)
#168번
변수1 = 0
print("168번")
for 변수 in range(1,11):
    변수1 += 변수
print(변수1)
#169번
변수1 = 0
print("169번")
for 변수 in range(1,11,2):
    변수1 += 변수
print(변수1)
#170번
변수1 = 1
print("170번")
for 변수 in range(1,11):
    변수1 *= 변수
print(변수1)