def get_binary_number(decimal_nnumber):
    assert isinstance(decimal_nnumber,int)
    return bin(decimal_nnumber)
print(get_binary_number(10))
print(get_binary_number("10"))