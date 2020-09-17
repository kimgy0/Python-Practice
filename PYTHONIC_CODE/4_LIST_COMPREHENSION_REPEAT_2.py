#중첩 반복문에서도 필터링을 적용할 수 있다. 다음과 같이 반목문 끝에 if문을 추가하면 된다.

case_1=["A","B","C"]
case_2=["D","E",'A']
result=[i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)