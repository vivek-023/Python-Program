# write Fibonacci series up to n
def fib(n):    
    a, b = 0, 1
    while b < n:
        print(b, end =" ")
        a, b = b, a+b


#import fibonacci module
import fibonacci 
num=int(input("\nEnter any number to print Fibonacci series "))
fibonacci.fib(num)
