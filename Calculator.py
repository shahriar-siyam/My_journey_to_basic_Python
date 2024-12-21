print("Choose two numbers here")
a=int(input())
b=int(input())
add="+"
sub="-"
mul="*"
div="/"
exp="**"
print("Select the operation you want")
op=input()
print("result")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="**":
    print(a**b)
