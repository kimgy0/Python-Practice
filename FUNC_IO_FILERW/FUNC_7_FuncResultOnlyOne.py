#함수의 반환값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b,a*b #튜플형식으로 하나로보고 반환해줌

result=sum_and_mul(3,4)#튜플형식으로 result에 저장
print(result)

#여기서 주의

first, second=sum_and_mul(3,4)
#이렇게하면 first와 second각각 a+b a*b저장
print(first)
print(second)