from stack_array import *


def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """

    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    
    operations = Stack(10)
    infix = infixexpr.split()
    rpn = ""
    if len(infix) == 1:
        return

    else:
        for i in range(len(infix)):
            if infix[i] == "+":
                if operations.num_items > 0:
                    if (
                            operations.peek() == "-" or
                            operations.peek() == "+"
                    ):
                        rpn += operations.pop()
                        rpn += " "
                        operations.push(infix[i])
                    else:
                        operations.push(infix[i])
                else:
                    operations.push(infix[i])

            elif infix[i] == "-":
                if operations.num_items > 0:
                    if (
                        operations.peek() == "+" or
                        operations.peek() == "-"
                    ):
                        rpn += operations.pop()
                        rpn += " "
                        operations.push(infix[i])
                    else:
                        operations.push(infix[i])
                else:
                    operations.push(infix[i])

            elif infix[i] == "*":
                if operations.num_items > 0:
                    if operations.peek() == "/":
                        rpn += operations.pop()
                        rpn += " "
                        operations.push(infix[i])
                    else:
                        operations.push(infix[i])
                else:
                    operations.push(infix[i])

            elif infix[i] == "/":
                if operations.num_items >0:
                    if operations.peek() == "*":
                        rpn += operations.pop()
                        rpn += " "
                        operations.push(infix[i])
                    else:
                        operations.push(infix[i])
                else:
                    operations.push(infix[i])

            elif infix[i] == "(":
                operations.push(infix[i])

            elif infix[i] == ")":
                while operations.peek() != "(":
                    rpn += operations.pop()
                    rpn += " "
                operations.pop()

            elif infix[i] == "^":
                operations.push(infix[i])

            else:
                rpn += infix[i]
                rpn += " "

        for i in range(operations.num_items):
            rpn += operations.pop()
            if operations.num_items != 0:
                rpn += " "
        return rpn



def postfix_eval(postfixExpr):
    """To evaluate the postfix expression"""
    stack = Stack(10)
    postfixExpr = postfixExpr.split()

    for i in range(len(postfixExpr)):
        if (
            postfixExpr[i] == "+" or
            postfixExpr[i] == "-" or
            postfixExpr[i] == "*" or
            postfixExpr[i] == "/" or
            postfixExpr[i] == "^"):
            value1 = stack.pop()
            value2 = stack.pop()
            stack.push(doMath(postfixExpr[i], value1, value2))
        else:
            stack.push(postfixExpr[i])
    return stack.peek()


def doMath(op, op1, op2):
    """To evaluate the math operations and return the results """
    if op == "+":
        return int(op2) + int(op1)
    elif op == "-":
        return int(op2) - int(op1)
    elif op == "*":
        return int(op2) * int(op1)
    elif op == "/":
        return int(op2) / int(op1)
    elif op == "^":
        return int(op2) ** int(op1)


def postfix_valid(postfixexpr):
    """Checks to see if the postfix expression is a balanced equation where
        if we have n operands, the amount of operators would be n - 1
        excluding parathesis"""
    nums = Stack(10)
    ops = Stack(10)
    para = Stack(10)
    postfixexpr = postfixexpr.split()

    for i in range(len(postfixexpr)):
        if (
            postfixexpr[i] == "+" or
            postfixexpr[i] == "-" or
            postfixexpr[i] == "*" or
            postfixexpr[i] == "/" or
            postfixexpr[i] == "^"
        ):
            ops.push(postfixexpr[i])

        elif (
            postfixexpr[i] == "(" or
            postfixexpr[i] == ")"
        ):
            para.push(postfixexpr[i])

        else:
            nums.push(postfixexpr[i])

    if nums.num_items - ops.num_items == 1:
        return True
    else:
        return False


print(postfix_valid("6 3 -"))