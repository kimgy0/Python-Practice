#점수로 합,불 따지기
marks=[90,25,67,45,80]

number=0
for mark in marks:
    number+=1
    if mark >= 60:
        print("{0}번 학생은 합격입니다.".format(number))
    else:
        print("{0}번 학생은 불합격입니다.".format(number))