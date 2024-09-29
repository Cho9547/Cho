# conditional_statement1.py

# if 문
#   if문은 주어진 조건이 참(True) 인 경우에만 특정 블록을 실행한다
#   if문은 조건을 검사하여 참 또는 거짓을 판별하고, 그 결과를 분기한다

""" 형식
if 조건 :
    print("실행할 코드 작성")
"""

# 사용할 수 있는 조건
#   변수의 값, 비교 연산, 논리 연산 등 결과가 True / False 반환되는 표현식이면 가능하다

number = 1

# if문
if number > 0:
    print("선택한 숫자는 '양수'입니다.")    # True기 때문에 프린트됨

# if-else문
#   조건이 참 / 거짓인 두 가지 경우를 각각 다른 코드블록이 실행되도록 하는 분기문이다.
if number > 0:
    print("선택한 숫자는 '양수'입니다.")  
else:
    print("선택한 숫자는 '음수'입니다.")

# if-elis-else 문
#   여러 조건을 순차적으로 검사하고, 조건 중 하나가 참인 경우 해당 코드 블록을 실행한다.
if number > 0:
    print("선택한 숫자는 '양수'입니다.")
elif number == 0:
    print("선택한 숫자는 0입니다.")
else:
    print("선택한 숫자는 '음수'입니다.")

# 구간에 따라 분기를 한다면 조건의 순서를 유의해야함
# 순차적으로 진행을 하는데, 상위 단계에서 True가 걸리면 아래를 처리하지 않음

# else 문을 사용하지 않아도 되는 케이스
# else 문은 필수가 아니기 때문에 필요한 상황에 적합하게(TF가 명확한 경우) 사용해야 한다.
gender = "남자"

if gender == "남자":
    print("남자 화장실은 우측입니다.")
else:
    print("여자 화장실은 좌측입니다.")
# 이 케이스엔, 남자, 여자 이외의 값을 입력했을 때 여자쪽으로 답변이 나옴


gender = "남자"

if gender == "남자":
    print("남자 화장실은 우측입니다.")
elif gender == "여자":
    print("여자 화장실은 좌측입니다.")
# 이 케이스엔 남자 여자 이외의 값을 입력했을 때 오류가 뜸

# 조건문의 조건의 순서
score = 85
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("E학점")

# 이렇게 분기를 한다면 문제될 게 없음

if score >= 70:
    print("C학점")
elif score >= 80:
    print("B학점")
# 이렇게 가는 순간 문제가 생김 --- 위에서부터 순차적으로 하기 때문

# 조건을 순서와 상관없이 나열하는 방법: 범위를 설정한다
if (score >= 70) and (score < 80):  # 근데 파이썬은 if 80 > score >= 70 으로 적어도 됨
    print("C학점")


print("프로그램 종료")   # 얜 if 문 안에 있는 게 아님