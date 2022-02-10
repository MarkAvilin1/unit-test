def calc(expression):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'The expiration should has one of ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except(ValueError, TypeError):
                raise ValueError('The expiration should has tow numbers and one sign')


if __name__ == '__main__':
    print(calc('5 - 2 - 1'))
