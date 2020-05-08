num = int(input("Enter any number: "))
check = num%2
if check == 0:
    print(num, "is an even number")
elif check == 1:
    print(num, "is an odd number")
else:
    print("Error, Invalid input")
