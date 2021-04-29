from stack import Stack


def reverse_string(a_string):

    stack = Stack()
    result = ""

    for char in a_string:
        stack.push(char)

    while not stack.is_empty():
        result += stack.pop()

    return result


print(reverse_string("Bonjour"))
