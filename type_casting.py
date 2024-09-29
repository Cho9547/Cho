# type_casting.py

# 자료형 변환
# 타입 확인하는 방법
#   type()을 사용하면 변수의 자료형을 확인할 수 있다
number_value = 1
string_value = "String"
sloat_value = 1.0

print("number_value 타입 = ", type(number_value))
print("string_value 타입 = ", type(string_value))
print("sloat_value 타입 = ", type(sloat_value))


# 정수형으로 변환하기
#   정수형으로 변환 가능한 데이터여야함
#   입력받은 데이터를 int()로 감싸준다
string_value = "10"
int_value = int(string_value)
print("string_value = ", type(string_value), "int_value = ", type(int_value))

bool_value = int(True)
print("bool_value 타입 = ", type(bool_value), "bool_value 값 = ", bool_value)

#------------------------------------------------------------------------
#### bool_value = int(input("True나 False를 입력하세요 >>>> "))
print("bool_value 타입 = ", type(bool_value), "bool_value 값 = ", bool_value)
# 여기서 입력된 True, False는 0, 1로 변환되는 True, False의 지위가 아닌 문자열 자체로의 True, False가 되는 것 같다

x = int(bool(input("입력 >> ")))
print(type(x), x)
# 이렇게 하면 True, False라는 문자로만 인식되던 애들리 불린값으로 변환이 되고, 얘는 정수형으로 인식이 가능해진다.
# 물론 이렇게 쓸 일이 거의 없긴 함
#------------------------------------------------------------------------


# 실수형으로 변환하기
#   실수형으로 변환이 가능한 데이터를
#   float()로 감싸주기
float_value = float("10.0")
print(type(float_value), float_value)

# 문자형으로 변환하기
#   str()로 감싸주기
str_value = str(10)
print(type(str_value), str_value + "10")
