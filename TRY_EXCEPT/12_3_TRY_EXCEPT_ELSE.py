for i in range(10):
    try:
        result=10/i
    except ZeroDivisionError:
        print("Not divided by 0")
    else:# 예외가 발생하지 않으면
        print(10/i)