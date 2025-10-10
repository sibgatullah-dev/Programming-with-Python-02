# This file will work as a module and the function fibo inside this module can be called which means we can create many functions in this file and call them according to our needs
def fibo_list(n):
    if n == 2 :
        return 1
    fib , fib2 = 1,1
    fib_list=[fib,fib2]
    for i in range(2,n):
        new_fib= fib+fib2
        fib_list.append(new_fib)
        fib = fib2
        fib2 = new_fib
    return fib_list


def fibo_num(n):
    fib_x = 1
    fib_next = 1

    for i in range(2,n):
        fib_new = fib_x+fib_next
        fib_x = fib_next
        fib_next = fib_new
    return fib_next   


if __name__ == "__main__":
    print(fibo_num(10))
    print(fibo_list(10))
