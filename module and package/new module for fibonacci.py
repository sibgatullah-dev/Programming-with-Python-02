def fibo(n):
    if n <= 2:
        return 1
    fib_x = 1
    fib_next = 1

   
    for i in range(2,n):
        fib_new = fib_x+fib_next
        fib_x = fib_next
        fib_next = fib_new
    return fib_next

for x in range(1,11):
    print(fibo(x))
        