rows=int(input("Enter the number of rows:"))
#outer loop for handle the number of rows
for i in range(rows):
    # inner loop for handle the number of columns
    #value is changing according to the outer loop
    for j in range(i+1):
        #printing stars
        print("*",end=" ")
    print()

