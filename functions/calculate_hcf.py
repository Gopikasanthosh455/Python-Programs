def calculate_hcf(x,y):
    if x<y:
        smallest=x
    else:
        smallest=y
    for i in range(1,smallest+1):
        if x % i ==0 and y % i==0:
            hcf = i
    return hcf
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("hcf =",calculate_hcf(num1,num2))