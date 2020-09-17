#별표는 곱하기 기호를 뜻한다. 별표는 기본 연산자로, 단순 곱셈이나 제곱연산에 많이 사용되었다.
#하지만 별표를 사용하는 특별한 경우가 있다. 바로 다음 코드와 같이
#함수의 가변 인수를 사용할 때 변수명 앞에 별표를 붙인다.

def asterrisk_test(a,*args):
    print(a,args)
    print(type(args))
print(asterrisk_test(1,2,3,4,5,6,7))
#반환은 튜플형식