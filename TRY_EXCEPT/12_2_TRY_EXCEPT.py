for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError as e:
        print("Not divided by 0")
        print(e) #사전에 정의