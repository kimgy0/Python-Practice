#f.close() 없이 자동으로 닫는 with문
with open("newFile.txt","w") as f:
    f.write("Life is too short, you need python")

f=open("newFile.txt",'r')
data=f.read()
print(data)
f.close()

