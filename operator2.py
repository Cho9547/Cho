# operator2.py

# 비교 연산자
# 두 개의 값을 비교하여 그 결과를 불린값(참/거짓, True, False)으로 변환하는 연산자이다.
# 조건문에서 많이 사용되고, 두 값 사이의 관계를 평가하는 코드에서 자주 사용한다.

print( 1 > 6) # False
print(10.7 > 10.6) # True
print("파이썬" == "파이썬") #문자열도 비교 가능함
print("python" == "Python")
print("python" != "Python")


#논리 연산자
#   하나 이상의 논리적 조건을 조합하여 새로운 논리 결과를 도출하는 데 사용된다.
#   조건문에서 많이 사용된다.
# and or not
print((10 > 5) and (10 > 6))
print((10 > 5) and (10 < 6))
print((10 < 5) and (10 > 6))
print((10 < 5) and (10 < 6))

print()

print((10 > 5) or (10 > 6))
print((10 > 5) or (10 < 6))
print((10 < 5) or (10 > 6))
print((10 < 5) or (10 < 6))

print()

print(not True) # True -> False
print(not False)


# 멤버십 연산자
#   주어진 값이 시퀀스 자료형인 문자열, 리스트, 튜플 등 특정 대상에 원하는 값이 포함되어 있는지 확인하는 연산자
print("a" in "apple") # 포함되어 있다.
print("a" in "Apple")
print("a" not in "apple") # 포함되어 있지 않다.

print(("a" and "p") in "apple") # 이렇게 해도 결과값이 나오긴 하는데, 아래처럼 쓰는 게 더 나음
print(("a" in "apple") and ("a" in "apple"))