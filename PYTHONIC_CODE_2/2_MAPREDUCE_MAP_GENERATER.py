#맵 함수는 연속 데이터를 저장하는 시퀀스형에서 요소마다 같은 기능을 적용할 때 사용한다.
#일반적으로 리스트나 튜플처럼 요소가 있는 시퀀스자료형에 사용된다.
#시퀀스형 데이터를 처리할 때 실행 시점의 값을 생성하여 효율적으로 메모리 관리할 수 있다는 장점.
#LIST를 이용해 실행시점에 메모리를 만들어 관리할 수 있다는 장점.
#MAP함수에는 LIST함수가 필요함.
#예를 들어 LIST함수를 쓰지 않는다면.
ex=[1,2,3,4,5]
f=lambda x:x**2

for value in map(f,ex):
    print(value)
    #리스트 함수를 쓰지 않는다면 map함수에서 value로 하나씩 받아와 출력해야한다.