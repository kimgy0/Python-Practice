#람다 함수
#def f(x,y):
#   return x,y
#   print(f(1,4))
#이렇게 써야 하는 함수가
#람다함수의 사용으로 밑에처럼 쓸수가 있다.
f=lambda x,y:x+y
print(f(1,4))

print((lambda x:x+1)(5))