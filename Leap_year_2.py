year=int(input("Year: "))
if year%400==0:
    print("Leap year")
elif year%4==0:
    if year%100==0:
        print("Not Leap-Year")
    else:
        print("Leap-Year it is")
else:
    print("Not Leap Year")
    print("The program was a success")
