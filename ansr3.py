import random

i=1
while (i<=10):
    r1=random.randint(0,9)
    print(r1)
    r2=random.randint(0, 9)
    print(r2)


    print(r1,"*",r2,"=")
    Answer=int(input("Enter the answer \n"))

    if Answer==r1*r2:
        print("Right!")

    else:
        print("Wrong!")

i=i=1