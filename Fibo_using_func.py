n=int(input("Enter a range"))
def fib(num):
    if num==0:
        return 0
    if num==1:
        return 1
    if num>1:
        return int(str(fib(num-1))+str(fib(num-2)))
fib(n)