"""
Several functions to handle infix to postfix conversions, postfix evaluations,
etc.

main function evaluates an expression from infix form.
"""

def evalPostfix(e):
    """
    Evaluate a postfix expression.
    """

    values = []

    for token in e:
        if token[0].isdigit():
            values.append(int(token))
            print(values)
            print(e)
        elif token == "u-":
            values.append(values.pop() * -1)
            print(e)
            print(values)
        elif token in ('*', '/', '-', '+', '^'):

            right = values.pop()
            left = values.pop()
            print(e)
            print(values)
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left *  right
            elif token == "/":
                result = left / right
            else:
                result = left**right
            values.append(result)

    return values[0]

def precedence(s):
    """
    Evaluate the precedence of an operator
    """
    if s == "+" or s == "-":
        return 1
    elif s == "*" or s == "/":
        return 2
    elif s in ("u+", "u-"):
        return 3
    elif s == "^":
        return 4
    else:
        return -1

def tokenize(s):
    """
    Tokenize a mathematical expression.
    """
    L = []

    n = 0
    while n < len(s):
        if s[n] == " ":
            n += 1
        elif s[n] in ('(', ')', '*', '/', '^', '-', '+'):
            L.append(s[n])
            n += 1
        elif s[n].isdigit():
            d= s[n]
            n += 1
            while n < len(s) and s[n].isdigit():
                d += s[n]
                n += 1
            L.append(d)

    return L

def unaryOps(L):
    """
    Identify unary operators in a list of token and replace them with u+ or u-.
    """
    if L[0] in ("+", "-"):
        L[0] = "u" + L[0]

    for n in range(1, len(L)):
        if L[n] in ("+", "-") and L[n-1] in ("+", "-", "*", "^", "/", "("):
            L[n] = "u" + L[n]

def inToPos(e):
    """
    Convert expression from infix to postfix form.
    """
    
    ops = []
    psfx = []

    token_e = unaryOps(tokenize(e))

    for n in token_e:
        if n.isdigit():
            psfx.append(n)
        elif n in ('*', '/', '^', '-', '+', "u+", "u-"):
            while len(ops) > 0 and ops[len(ops) - 1] != "(" and\
                precedence(n) < precedence(ops[len(ops) - 1]):
                    psfx.append(ops.pop())
            ops.append(n)
        elif n == "(":
            ops.append(n)
        elif n == ")":
            while ops[len(ops) - 1] != "(":
                psfx.append(ops.pop())
            ops.remove("(")

    while len(ops) > 0:
        psfx.append(ops.pop())

    return psfx


def main():

    prompt = "Enter a mathematical expression in infix form:\n\t>  "

    e = input(prompt)
    while True:
        if e.count("(") != e.count(")"):
                print("This is not a correct expression. Try again.")
                e = input(prompt)
        else:
            break
    print(e)
    e = inToPos(e)
    print(e)
    print(f"The value of this expression is {evalPostfix(e)}.")

if __name__ == "__main__":
    main()
