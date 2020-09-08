#함수 안에서 함수밖의 변수를 변경하는 방법
a=1
def vartest():
    global a #전역변수 a를 가리킴
    a=a+1 #그리고 a에 대한 덧셈 수행

vartest()
print(a)