#리스트 컴프리헨션에도 기존처럼 리스트 2개를 섞어 사용할 수 있다.
#다음 코드와 같이 2개의 FOR문을 만들 수 있다.
word_1="Hello"
word_2="World"
result=[i+j for i in word_1 for j in word_2]

print(result)