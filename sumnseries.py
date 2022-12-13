from tuple import factorial
def sum_series(x, n):
    sum = 0
    for i in range(1, n+1, 1):
        term = ((-1)**(i+1))*(x**(2*i-2)/factorial(2*i-2)) #Calculating nth term
        sum += term
    return sum

if __name__ == "__main__":
    n = int(input("Enter n: "))
    x = int(input("Enter x: "))
    sum = sum_series(x, n)
    print("\nSum of",n,"terms of series for x=",x,":",sum)
