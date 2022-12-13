def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    num =  int(input("Enter a number: "))
    print("fibonacci series upto",num,"term: ",fib(num))
    print("factorial of",num,"is:",factorial(num))
