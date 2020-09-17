#필터링은 IF문과 함께 사용하는 리스트 컴프리헨션이다. 일반적으로 짝수만 저장하기 위해서는 다음과 같은 코드를 작성해야 한다.

result=[i for i in range(10) if i%2==0]
print(result)