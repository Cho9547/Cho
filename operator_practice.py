number = 45
tens = number // 10
units = number % 10
print("십의 자리", tens, sep= " : ")  #sep 활용해서 같은 꼴 만들기
print("일의 자리 :", units)


total_seconds = 3690
hours = total_seconds // 3600
remaining_seconds = total_seconds - 3600 * hours
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("시 :", hours)
print("분 :", minutes)
print("초 :", seconds)

minutes = total_seconds // 60 // 60 # 이렇게 하면 r.s의 개입 없이도 한번에 구할 수 있음
print(minutes)
seconds = total_seconds % 60 # 생각해 보니까 초는 그냥 처음부터 60으로 나눈 나머지 로 구해도 된다
print(seconds)

print(f"{hours}시간 {minutes}분 {seconds}초") # f-strings

print(hours, "시간", minutes, "분", seconds, "초")





## 그럼 문자를 숫자로 변형할 수 있나?


total_seconds = input("몇 초입니까? ")

hours = total_seconds // 3600
remaining_seconds = total_seconds - 3600 * hours
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("시 :", hours)
print("분 :", minutes)
print("초 :", seconds)

print(f"{hours}시간 {minutes}분 {seconds}초")
