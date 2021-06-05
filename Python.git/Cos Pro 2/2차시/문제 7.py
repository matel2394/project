def solution(value,unit):
    convarted = 0
    if unit == "C":
        value = value * 1.0 * 32
    if unit == "F":
        value = value - 32 /1.8
    convarted = int(value)
    return convarted

value = 527
unit = "C"
ret = solution(value,unit)

print(ret)