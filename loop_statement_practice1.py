# loop_statement_practice1

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print(number)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if int(number) % 2 == 0:   # 이거 == 계속 틀린다
        print(f"{number}는 짝수입니다")
    else:
        print(f"{number}는 홀수입니다")

print("=================while문=================")


numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
index = 0 # 시작 인덱스를 0으로 초기화합니다 (얘도 안 하니까 오류나네)

while index < len(numbers): # imdex가 numbers의 길이보다 작은 동안 반복합니다
    number = numbers[index]
    if number % 2 == 0:
        print(f"{number}은 짝수입니다")
    else:
        print(f"{number}은 홀수입니다")

    index += 1  ### 얘가 매우 중요!! 얘를 안 하니까 273에서 머물러서 273만 연산했다!!



numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    print(f"{number}은 {len(str(number))} 자릿수입니다")   # type casting으로 숫자를 문자로 변형하고, 그 자리수를 구하는 방식  0