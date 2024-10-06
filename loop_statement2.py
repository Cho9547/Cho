# loop_statement2

# while 문 ___ 조건이 개입이 된다면 while 문으로
count = 0

while count < 5:
    print(count)

    # 카운터 변수의 상태 변화를 꼭 적어줘야함 !!!!!
    count += 1 # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 중요

# 상태 기반으로 while 반복문 사용하기
numbers = [1, 2, 1, 2]
value = 2

while value in numbers:
    numbers.remove(value)
print(numbers)

# 시간 기반으로 while 반복문 사용하기
import time

target_time = time.time() + 5 # 현재(실행 당시)로부터 5초 이후를 뜻함 
number = 0 

while time.time() < target_time:
    number += 1
print(f"5초 동안 {number}번 반복했습니다")

# sleep() 함수와 time 모듈 함께 사용하기

number = 0
duration = 5

while duration > 0:
    number += 1
    time.sleep(1)
    duration -= 1
print(f"sleep()을 사용한 5초 동안 {number}번 반복했습니다")