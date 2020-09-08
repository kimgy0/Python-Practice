#매개 변수에 초깃값 미리 설정하기
def say_myself(name,old,man=True):
    #초기값 설정시 주의사항 (name,man=True,old) 이런식으로 인자가 바뀌지 않게 주의
    #교재 164페이지 참고
    #영상강의 9:58초
    print("나의 이름은 {0} 입니다.".format(name))
    print("나의 나이는 %d살 입니다." %old)

    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("김규영",23)
say_myself("김규영",23,True)