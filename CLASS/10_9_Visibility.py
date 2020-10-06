class Product(object):
    pass


class Inventory(object):
    def __init__(self):
        self.__items = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

    @property
    def items(self):
        return self.__items

    # 이렇게 하면 __가 붙어도 직접적으로 인스턴스로 직접 꺼내는 것이 가능.


myinventory = Inventory()
items = myinventory.items
items.append(Product())
print(myinventory.get_number_of_items())
