from stack_array import *


def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """

    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    
    """Variables:   operations = a stack of size 10
                    infix = tokens of the string infix expression
                    rpn = the postfix expression """
    operations = Stack(10)
    infix = infixexpr.split()
    rpn = ""
    if len(infix) == 1:
        return infixexpr

    else:
        for i in range(len(infix)):
            if infix[i] == "+":
                if operations.num_items > 0:
                    if (                                # if statement used to start popping operations off the stack
                        operations.peek() == "-" or     # and appending the operation to the rpn string when there are
                        operations.peek() == "+" or     # more than one operations
                        operations.peek() == "*" or
                        operations.peek() == "/"
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
                    if (                                # if statement used to start popping operations off the stack
                        operations.peek() == "+" or     # and appending the operation to the rpn string when there are
                        operations.peek() == "-" or     # more than one operations
                        operations.peek() == "*" or
                        operations.peek() == "/"
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
                    if (
                        operations.peek() == "/" or     # if statement used to start popping operations off the stack
                        operations.peek() == "*"        # and appending the operation to the rpn string when there are
                    ):                                  # more "*" and "/" operations
                        rpn += operations.pop()
                        rpn += " "
                        operations.push(infix[i])
                    else:
                        operations.push(infix[i])
                else:
                    operations.push(infix[i])

            elif infix[i] == "/":
                if operations.num_items > 0:
                    if (
                        operations.peek() == "*" or     # if statement used to start popping operations off the stack
                        operations.peek() == "/"        # and appending the operation to the rpn string when there are
                    ):                                   # more "*" and "/" operations
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
                while operations.peek() != "(":     # when the close paranthesis is found, all items in the operations
                    rpn += operations.pop()         # stack is popped and appended to the rpn string until the open
                    rpn += " "                      # paranthesis is found and discarded alonged with the closed
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

print(infix_to_postfix("4 + 2 * 3 * 4"))

def postfix_eval(postfixExpr):
    """To evaluate the postfix expression"""

    """Signature:  a string containing an postfix expression where tokens are space separated is
       the single input parameter and returns an int value containing a postfix expression's evaluated 
       output """

    """Variables:   stack = a stack of size 10
                    postfixExpr = tokens of the string postfix expression """
    stack = Stack(10)
    postfixExpr = postfixExpr.split()

    for i in range(len(postfixExpr)):
        if (  # two values are popped off the stack with the operator and the result is pushed back onto the stack
            postfixExpr[i] == "+" or
            postfixExpr[i] == "-" or
            postfixExpr[i] == "*" or
            postfixExpr[i] == "/" or
            postfixExpr[i] == "^"
        ):
            value1 = stack.pop()
            value2 = stack.pop()
            stack.push(doMath(postfixExpr[i], value1, value2))
        else:
            stack.push(postfixExpr[i])
    return stack.peek()


def doMath(op, op1, op2):
    """To evaluate the math operations and return the results """

    """Signature: Three strings containing the operator and two values are the input parementers
        and returns an int value containing the value of the math expression used """

    if op == "+":
        return int(op2) + int(op1)
    elif op == "-":
        return int(op2) - int(op1)
    elif op == "*":
        return int(op2) * int(op1)
    elif op == "/":
        if int(op1) == 0:
            raise ValueError
        else:
            return int(op2) / int(op1)
    elif op == "^":
        return int(op2) ** int(op1)


def postfix_valid(postfixexpr):
    """Checks to see if the postfix expression is a balanced equation where
        if we have n operands, the amount of operators would be n - 1
        excluding parenthesis"""

    """Signature: a string containing an postfix expression where tokens are space separated is
       the single input parameter and returns a boolean whether the expression is a valid or 
        invalid postfix expression """

    """Variables:   nums = a stack that is used to push numeric values to
                    ops = a stack that is used to push operations to
                    para = a stack that is used to push paranthesis on as they are not needed
                    postfixexpr = tokens of the string postfix expression """

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

        elif (      # paranthesis found in the postfix expressions are pushed on the para stack to not be used
            postfixexpr[i] == "(" or
            postfixexpr[i] == ")"
        ):
            para.push(postfixexpr[i])

        else:
            nums.push(postfixexpr[i])

    if nums.num_items - ops.num_items == 1:     # an expression is valid when there are more one less operator than nums
        return True
    else:
        return False


