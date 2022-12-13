num = int(input("Enter a number greater than or equal to 10: "))

if num >= 10:
    set_i = set()
    while num != 0:
        set_i.add(num%10)
        num = int(num/10)
    print("Set: ", set_i)
else:
    print("Oops! Number is less than 10")
