from typing import List
from numbers import Number


ops = {'+', '-', '*', '/'}


def rec_parse(tokens: List[str]) -> List[str]:
    stack = []
    token_iter = iter(tokens)
    for i in token_iter:
        if i == '(':
            j = next(token_iter)
            block = [j]
            while not j == ')':
                j = next(token_iter)
                block.append(j)
            stack.append(rec_parse(block[:-1]))
            continue
        if i in ops:
            k = next(token_iter)
            try:
                float(k)
            except:
                raise Exception(f'Invalid expression: last token \'{k}\' should be a number')
            stack.append(k)
            stack.append(i)
        else:
            try:
                float(i)
            except:
                raise Exception(f'Invalid expression: {i} should be a number')
            stack.append(i)
    return stack


def parse_expr(expr: str) -> List[str]:
    return rec_parse(expr.split())


def add(*nums: Number) -> Number:
    sum = 0
    for n in nums:
        sum += n
    return sum


def sub(left: Number, right: Number) -> Number:
    return left - right


def mult(*nums: Number) -> Number:
    prod = 1
    for n in nums:
        prod *= n
    return prod


def div(divisor: Number, dividend: Number) -> Number:
    if dividend == 0:
        raise Exception('Can\'t divide by zero!')
    return divisor/dividend
