#191번
print("191번")
이차원1 =[[2000,3050,2050,1980],
        [7500,2050,2050,1980],
        [15450,15050,1550,14900]]
for 변수 in 이차원1:
    for 변수1 in 변수:
        print(변수1 * 1.00014)
#192번
print("192번")
이차원1 =[[2000,3050,2050,1980],
        [7500,2050,2050,1980],
        [15450,15050,1550,14900]]
for 변수 in 이차원1:
    for 변수1 in 변수:
        print(변수1 * 1.00014)
    print("-"*4)
#193번
print("193번")
리스트1 =[]
이차원1 =[[2000,3050,2050,1980],
        [7500,2050,2050,1980],
        [15450,15050,1550,14900]]
for 변수 in 이차원1:
        for 변수1 in 변수:
            리스트1.append(변수1 * 1.00014)
print(리스트1)
#194번
print("194번")
이차원2 = []
for 변수 in 이차원1:
    이차원3 = []
    for 변수1 in 변수:
        이차원3.append(변수1 * 1.00014)
    이차원2.append(이차원3)
print(이차원2)
#195번
print("195번")
이차원4 = [["open","high","low","close"],
         [100,110,70,100],[200,210,180,190],
         [300,310,300,310]]
for 변수 in 이차원4[1:]:
        print(변수[3])
#196번
print("196번")
이차원4 = [["open","high","low","close"],
         [100,110,70,100],[200,210,180,190],
         [300,310,300,310]]
for 변수 in 이차원4[1:]:
    if 변수[3] > 150:
        print(변수[3])
#197번
print("197번")
이차원4 = [["open","high","low","close"],
         [100,110,70,100],[200,210,180,190],
         [300,310,300,310]]
for 변수 in 이차원4[1:]:
    if 변수[3] >= 변수[0]:
        print(변수[3])
#198번
print("198번")
리스트4 = []
이차원4 = [["open","high","low","close"],
         [100,110,70,100],[200,210,180,190],
         [300,310,300,310]]
for 변수 in 이차원4[1:]:
    리스트4.append(변수[1] - 변수[2])
print(리스트4)
#199번
print("199번")
이차원4 = [["open","high","low","close"],
         [100,110,70,100],[200,210,180,190],
         [300,310,300,310]]
for 변수 in 이차원4[1:]:
    if 변수[3] > 변수[0]:
        print(변수[1] - 변수[2])
#200번
print("200번")
이차원4 = [["open","high","low","close"],
         [100,110,70,100],[200,210,180,190],
         [300,310,300,310]]
for 변수 in 이차원4[1:]:
        print(변수[3] - 변수[0])
