#별표는 곱하기 기호를 뜻한다. 별표는 기본 연산자로, 단순 곱셈이나 제곱연산에 많이 사용되었다.
#하지만 별표를 사용하는 특별한 경우가 있다. 바로 다음 코드와 같이
#함수의 가변 인수를 사용할 때 변수명 앞에 별표를 붙인다.

def asterrisk_test(a,**kwargs):
    print(a,kwargs)
    print(type(kwargs))
print(asterrisk_test(1, b=2,c=2,d=4,e=5))


#반환은 딕셔너리