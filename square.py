print("Here are the sides")
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
d=int(input("D="))
print("Here are the Angles")
ang1=int(input("<A="))
ang2=int(input("<B="))
ang3=int(input("<C="))
ang4=int(input("<D="))
check1=(a==b==c==d)
check2=(ang1==90 and ang2==90 and ang3==90 and ang4==90)
if check1==check2:
 print("It's a square")
else:
     print("not a square")


