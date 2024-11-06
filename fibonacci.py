"""
# this is non recursive approach
def fibonacci_iterative():
     n = int(input("enter number: "))
     if n <= 0:
         return 0
     elif n == 1:
         return 1
     else:
         a, b = 0, 1
         print("a=",a,"b=",b)
         for i in range(2, n):
             c = a + b
             a = b
             b = c
             print("a=",a,"b=",b)
         return b

print(fibonacci_iterative())

"""
# this is recursive approach
def fibonacci_recursive(n):
     if n <= 0:
         return 0
     elif n == 1:
         return 1
     else:
         #print(n)
         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(int(input("enter number: "))))

