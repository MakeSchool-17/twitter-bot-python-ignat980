def set_bit(x, position):
    mask = 1 << position
    return x | mask


def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask


def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask


def is_bit_set(x, position):
    shifted = x >> position
    return shifted & 1


def modify_bit(x, position, state):
    mask = 1 << position
    return (x & ~mask) | (-state & mask)


def is_even(x):
    return ~(x & 1)


def is_odd(x):
    return x & 1


def is_power(x):
    return (x & x - 1) == 0


def count_different(x, y):
    print('In different func', sep='')
    print(bin(x), ', X', sep='')
    print(bin(y), ', Y', sep='')
    different = x ^ y
    print(bin(different), ', x ^ y', sep='')
    count = 0b0
    while different > 0:
        count += different & 1
        different = different >> 0b1
    return count


if __name__ == '__main__':
    x = 0b01101001
    y = -0b01010100
    print(bin(x), ', X', sep='')
    print(bin(y), ', Y', sep='')
    print(x, ', X', sep='')
    print(y, ', Y', sep='')
    print(bin(set_bit(x, 0b1)), ', Set x\'s 2nd bit', sep='')
    print(bin(clear_bit(x, 0b11)), ', Clear x\'s 4th bit', sep='')
    print(bin(flip_bit(x, 0b100)), ', Flip x\'s 5th bit', sep='')
    print(bool(is_bit_set(x, 0b100)), ', Is x\'s 5th bit set?', sep='')
    print(bool(is_bit_set(x, 0b11)), ', Is x\'s 4th bit set?', sep='')
    print(bin(modify_bit(x, 0b0, 0b0)), ', Modify x\'s 1st bit to 0', sep='')
    print(bin(y), ', Y', sep='')
    print(y, ', Y as int', sep='')
    print(bool(is_power(y)), ', Is Y a power of two', sep='')
    print('There are ', count_different(x, y), ' different bits between x and y.', sep='')
