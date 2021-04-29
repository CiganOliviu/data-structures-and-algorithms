from stack import Stack

def convert_int_to_bin(dec_num):

    stack = Stack()
    rest = 1
    result = ""

    while dec_num > 0:

        rest = dec_num % 2
        stack.push(rest)

        dec_num //= 2

    while not stack.is_empty():
        result += str(stack.pop())

    return result


print(convert_int_to_bin(321))
