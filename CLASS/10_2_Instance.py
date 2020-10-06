class SoccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name=name
        self.position=position
        self.back_number=back_number

    def change_back_number(self,new_number):
        print("선수의 등번호를 변경한다 : From {0} to {1}".format(self.back_number,new_number))
        self.back_number=new_number

    def __str__(self):
        return "Hello, My name is {0} I play in {1} in center".format(self.name, self.position)

Jihyun = SoccerPlayer("Jihyun","MF",10)
print("현재 선수의 등번호는",Jihyun.back_number)
Jihyun.change_back_number(5)
print("현재 선수의 등번호는",Jihyun.back_number)