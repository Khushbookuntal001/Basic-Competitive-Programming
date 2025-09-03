N= int (input("Enter a Number: "))
for i in range (N+1):
    for j in range (i):
        print("*", end= " ")
    print()