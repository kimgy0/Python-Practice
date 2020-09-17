#일반적으로 짝수만 저장하기 위해서는 다음과 같은 코드를 작성해야 한다.
result=[]
for i in range(10):
    if i%2 == 0:
        result.append(i)

print(result)