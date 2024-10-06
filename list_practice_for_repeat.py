# list_practice_for_repeat

hyun = input("현우의 턱걸이 횟수를 입력해주세요. >>>")
ji = input("지영이의 턱걸이 횟수를 입력해주세요. >>>")
dong = input("동혁이의 턱걸이 횟수를 입력해주세요. >>>")
sang = input("상준이의 턱걸이 횟수를 입력해주세요. >>>")

record = [hyun, ji, dong, sang]
print(record)

avg = (int(record[0]) + int(record[1]) + int(record[2]) + int(record[3])) / 4

print(round(avg, 2))


count = int(input("현우의 턱걸이 횟수를 입력하세요. >>> "))
record.append(count)
count = int(input("지영의 턱걸이 횟수를 입력하세요. >>> "))
record.append(count)
count = int(input("동혁의 턱걸이 횟수를 입력하세요. >>> "))
record.append(count)
count = int(input("상준의 턱걸이 횟수를 입력하세요. >>> "))   # 학생의 이름을 빼고는 완벽한 반복문
record.append(count)

total = sum(record)   # 단 record의 항들이 숫자의 데이터여야함. 즉, int를 input 바로 밖에 써야됨

avg = total / len(record)
print(round(avg))   # 이렇게 하면 정수까지