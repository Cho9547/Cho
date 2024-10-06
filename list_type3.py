# list_type3

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# + 연산자
list_c = list_a + list_b
print(list_c)

# * 연산자
list_d = list_a * 3   # 여기서 *는 반복을 뜻함
print(list_d)

list_e = [*list_a]   # 여기서 *는 전개를 뜻함
print(list_e)



#################################################################################################
# 리스트 요소 추가하기

string_list = ["안", "녕", "하", "세", "요"]

# append() : 마지막에 데이터 하나 추가
string_list.append("?")
print(string_list)

# insert() : 특정 위치에 데이터 하나 추가
string_list.insert(2, "!")  # (결과가 되는?)인덱스, 값
print(string_list)

# extend() : 여러 개의 데이터를 추가
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)

# +랑 어떻게 다를까?
# 파괴적인 함수, 비파괴적인 함수
# +는 새로운 리스트를 만들면서 원본을 바꾸지 않음 (비파괴적)
# extend는 원본 자체를 바꿈 (파괴적)
# 가급적 비파괴적인 게 낫지만, 원본과 결과를 모두 사용하는 게 메모리에 부담이 되는 경우 파괴적으로 사용하는 게 나을 수 있음




################################################################################################
# 리스트 요소 삭제하기
#   인덱스로 제거 / 값으로 제거

#   인덱스로 제거 (del)
del list_b[1]
print(list_b)

list_b = [4, 5, 6]
del list_b[1:3]    ####[:1] [1:] [0: -1] [:] 모두 해보기!!!
print(list_b)

#   인덱스로 제거 (pop())
list_b = [4, 5, 6]
result = list_b.pop(1)
print(list_b)      # pop()은 삭제한 값을 반환해줌
print(result)

#   값으로 제거 (remove())
list_b = [4, 5, 4, 6]
list_b.remove(4) # 중복된 값이 있는 경우 맨 앞의 인덱스만 제거한다
print(list_b)

#   전체 제거 (clear())
list_b = [4, 5, 6]
list_b.clear()
print(list_b)