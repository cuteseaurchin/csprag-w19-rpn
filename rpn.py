#!/usr/bin/env python3

def calculate(arg):
    stack = []
    tokens = arg.split()
    firstOperand = tokens[0]
    tokens.pop(0)
    secondOperand = tokens[0]
    tokens.pop(0)
    operator = tokens[0]
    tokens.pop(0)
    if operator == '+':
        tokens.insert(0, (str)((int(firstOperand)) + (int(secondOperand))))
    elif operator == '-':
        tokens.insert(0, (str)((int(firstOperand)) - (int(secondOperand))))
    return int(tokens[0])
    pass

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
