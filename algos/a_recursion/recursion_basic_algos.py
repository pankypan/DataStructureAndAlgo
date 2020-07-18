def fib(n):
    """实现斐波那契数列求值f(n)=f(n-1)+f(n-2)"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def factorial(n):
    """递归实现求阶乘n!"""
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    print(fib(5))

    print(factorial(4))
    print(factorial(5))
