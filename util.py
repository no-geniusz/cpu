def to_bit(value):
    if value == None:
        return 'X'
    else:
        return str(int(value))

def to_bit_arr(arr):
    return "".join(map(lambda value: to_bit(value), arr))
