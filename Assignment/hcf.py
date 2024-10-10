def calculate_hcf(x,y):
    if x<y:
        smallest=x
    else:
        smallest=y
    for i in range(1,smallest+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
num=int(input("Enter first number: "))
num1=int(input("Enter second number: "))
print("HCF  :",calculate_hcf(num,num1))