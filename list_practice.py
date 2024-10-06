# list_practice

class_a = ["현우", "지영", "동혁"]

class_a.append("상준")   # (insert(3, "상준"))으로 해도 되긴 함
print(class_a)

# class_a[0] = "현석"    # 0번 인덱스에 접근 후에, 그 값 자체를 "현석"으로 바꾸는 것이다. 다만 얘는 "현우"를 "현석"으로 바꾸는 것이 아니라, 0번 인덱스를 현석으로 바꾸는 것이기 때문에 덜 유연하다
result = class_a.index("현우")    # 정렬이 어떻게 돼 있든, 리스트 안의 현우의 인덱스를 가지고 옴
print(result)    # 현우의 현재 인덱스를 출력
class_a[result] = "현석"    # 현우의 인덱스 자리를 현석으로 대체 => '값'인 현우를 '현석'으로 바꾸는 것이 아니라, 현우의 인덱스를 유연하게 찾고 그것을 현석으로 바꾼다
print(class_a)

print(class_a[1:3])

print(class_a[-1])


class_a = ["현우", "지영", "동혁"]
class_b = ["삼영", "재석", "기영", "영자"]

class_a.extend(class_b)
print(class_a)

class_a.sort(reverse=True)
print(class_a)

result = class_a.index("동혁")
class_a.pop(result)         # 지금 보니까 이런 애들은 class_a = 이렇게 새롭게 정의를 안 해도 그냥 class_a를 파괴하면서 리스트를 변형시킴    여태까지 했던 함수들과는 다르게, 파괴적 함수는 재정의를 할 필요 없이 입히기만 하면 됨
print(class_a)

## class_a.remove("동혁")로 가도 됨