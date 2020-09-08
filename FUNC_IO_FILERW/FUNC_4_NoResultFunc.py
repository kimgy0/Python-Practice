#결과 값이 없는 함수1
def sum(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))
sum(3,4)

print(sum(3,4))
#단, 함수가 한번이라도 실행되면서 함수내 print구문은 실행됨.
#위 print(sum(3,4))의 문장은 None이라고 출력함.