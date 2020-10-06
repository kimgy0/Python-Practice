class Product(object):
    pass

class Inventory(object):

    def __init__(self):
        self.__items=[]
        #__은 외부에서 인스턴스로 직접접근을 하지 못하게 막는다.

    def add_new_item(self,product):
        if type(product)==Product:
            self.__items.append(product)
            print("add new item")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

myinventory=Inventory()
myinventory.add_new_item(Product())
myinventory.add_new_item(Product())
myinventory.add_new_item(Product())
print(myinventory.get_number_of_items())
#단, myinventory.__items 로는 접근이 불가능하다.