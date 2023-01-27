a=int(input("Enter the year \n "))

if a%4==0:
    if a%100==0 and a%400!=0:
        print("It is not a leap year")

    else:
        print("It is  a leap year")


else:
    print("It is  a leap year")