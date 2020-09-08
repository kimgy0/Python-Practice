#함수 안에서 선언된 변수의 효력범위

a=1
def vartest(a):
    a=a+1
    return a
#만약 return이 없을시
#함수만의 변수이며 함수가 끝나면 없어진다. 함수밖의 변수가 아니다.
#즉 a는 2가 아니라 1이다(함수 밖의 변수).

a=vartest(a)
print(a)