try:
    x=int(input("Enter a integer:"))
    print("Entered integer:",x)
except ValueError :
    print("ValueError, The input is not a valid integer!")