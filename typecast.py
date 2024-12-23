#typecasting
a="2"
b="1"
print(a+b)
print(float(a)+int(b))
c=float(a)+int(b)
d=int(a)+int(b)
print(type(c))
print(type(d))


# input related
a=input("Give me a number: ") # we take 5
print("The number you have put is ",a)
b=input("Give me another number: ") # we take 6
print("Sum of that number is ",a+b) #it is 56 because it is concatenated as string
print("Sum of that number is ",int(a+b)) #it is 56 cause at first it concatenated as string then it is printed as integer
print("Sum of that number is ",int(a)+int(b)) #it is taken as integers
print("Sum of that number is ",int(a+b)+5)

# different operation with string
# a=input()
# b=input()
# print(a+b)
# print(a-b) #error
# print(a*b) #error
# print(a/b) #error