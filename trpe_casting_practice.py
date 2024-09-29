year = int(input("현재 연도를 입력하세요 >>> "))
birth = int(input("태어난 연도를 입력하세요 >>> "))
age = year - birth
print(f"현재 나이는 {age}입니다.")

# 내가 직접 넣는 것이 아니라, 자동으로 가져오는 기능이 있다!!

from datetime import datetime


birth = int(input("태어난 연도를 입력하세요 >>> "))
age = (datetime.now().year) - birth
print(f"현재 나이는 {age}입니다.")
