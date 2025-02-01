hour=int(input("Hour: "))
minute=int(input("Minutes: "))
sec=int(input("Seconds: "))

def time(h,m,s):
    if h>24:
        h=h-24
    if m>60:
        m=m-60
        h=h+1
    if s>60:
        s=s-60
        m=m+1
    if 0<=h<=12:
        print(h,":",m,":",s)
        if h==12 and s>0:
            print("Good Afternoon")
        else:
            print("Good Morning")
    elif 12<h<=15:
        print(h, ":", m, ":", s)
        if h==15 and s>0:
            print("Good Evening")
        else:
            print("Good Afternoon")
    elif 15<h<=18:
        print(h, ":", m, ":", s)
        if h==18 and s>0:
            print("Good Night")
        else:
            print("Good Evening")
    elif 18<h<=24:
        print(h, ":", m, ":", s)
        if h==24 and s>0:
            h=0
            print(h, ":", m, ":", s)
            print("Good Morning")
        else:
            print(h, ":", m, ":", s)
            print("Good Night")
    return 0



time(hour,minute,sec)