number = int(input("숫자를 입력해주세요. >>> "))
x = number % 2
if number == 0:
    print("입력하신 숫자는 0입니다.")
elif x == 1:
    print("입력하신 숫자는 홀수입니다.")
elif x == 0:    #이 항목에선 else로 가도 되긴 함, x==0이 아니라, x!=1로 가도 됨
    print("입력하신 숫자는 짝수입니다.")