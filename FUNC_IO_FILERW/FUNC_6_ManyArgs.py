#여러개의 입력값 받기
def sum_many(*args): #args는 입력된 인자들을 튜플형식으로 바꿔줌.
    sum=0
    for i in args:
        sum = sum + i
    return sum

result=sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

