number = input("Enter a number please \n")
if  number.isdigit() == True :
    c = 0
    for b in number:
        b = int(b)
        c += b**len(number)
    number = int(number)
    if c == number:
        print ("{} is an amstrong number.".format(number))
    else: 
        print ("{} is not an amstrong number.".format(number))
elif number[0] == "-" :
    print("Please enter a positive number")
elif "." in number or "," in number: 
    print("Please enter an integer number")
else : print("Do not use any entries other than numeric values")
