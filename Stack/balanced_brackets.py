from stack import Stack


def is_not_match(bracket1, bracket2):

    if bracket1 == "(" and bracket2 == ")":
        return False

    if bracket1 == "[" and bracket2 == "]":
        return False

    if bracket1 == "{" and bracket2 == "}":
        return False

    return True



def is_paranthesis_balanced(paranthesis_sequence):

    stack = Stack()
    index = 0

    for index in paranthesis_sequence:
        bracket = index

        if bracket in "{[(":
            stack.push(bracket)
        else:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()

                if is_not_match(top, bracket):
                    return False

    if stack.is_empty():
        return True

    return False

assert(is_paranthesis_balanced("(((({}))))") == True)
assert(is_paranthesis_balanced("[][]]]") == False)
assert(is_paranthesis_balanced("[][]") == True)
