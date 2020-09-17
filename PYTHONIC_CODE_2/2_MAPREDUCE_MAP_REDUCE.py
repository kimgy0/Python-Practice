#맵 함수와 용법은 다르지만 형제처럼 사용할 수 있는 함수
#리듀스 함수는 리스트와 같은 시퀀스자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수이다.

from functools import reduce

ex=[1,2,3,4,5]

print(reduce(lambda x,y:x+y,ex))
x=0
#result=sum([x+y for x in range(1) for y in ex])
#영상에서 리스트 컴프리헨션으로 만들어보라고 하셔서 주석 씌워놨습니다!
#공부용으로 그냥 적어놨습니다!
#print(result)

h=0
for i in ex:
    h=h+i
print(h)
#위 식과 for 문과의 같은 역할