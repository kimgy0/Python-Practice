#필터링은 IF문과 함께 사용하는 리스트 컴프리헨션이다.

result=[i if i%2==0 else 10 for i in range(10)]
# else를 적어서 앞에서 if else문을 적어준다.
print(result)