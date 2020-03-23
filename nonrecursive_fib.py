def fib(n):
""" non recursive way is always better """
    a = 0
    b = 1
    while n - 2:
        c = a+b
        a = b
        b = c
        n = n-1
    print(c)

x = int(input("sm"))
fib(x)
