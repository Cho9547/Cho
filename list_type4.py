# list_type4

# 리스트의 다량한 사용법

numbers = [2, 4, 1, 6, 10]

#   sort()
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#   멤버쉽 연산자
print(1 in numbers)
print(1 not in numbers)

#   index()
#   존재하지 않는 값은 ValueError 발생한다
result = numbers.index(10)
print(result)