# loop_statement_practice2

todo_list = []   # 할 일 목록을 저장할 빈 리스트 생성
user_input = ""    # 사용자 입력을 저장할 빈 문자열 생성(초기화)
while user_input.lower() != "quit":    # while은, False가 될 떄까지 돌아가는 거다. ~인 한 계속 해라 라는 뜻
    user_input = input("Todo list를 입력하세요. 종료하려면 quit을 입력하세요 >>> ")
    if user_input.lower() != "quit":    # quit에 ""를 쳐줘야 문자로서 인식을 해줄 수 있음
        todo_list.append(user_input)

# 여기까지는 입력 받기 완료
# 내가 input을 보고 이게 프린트가 된 걸로 착각했는데, 여기까지는 그냥 정보를 받는 것까지만 한 것이다

count = 1
for todo in todo_list:
    print(f"할 일 목록({count}) : {todo}")
    count += 1



# 이거 좀 빡시게 복습해보자

