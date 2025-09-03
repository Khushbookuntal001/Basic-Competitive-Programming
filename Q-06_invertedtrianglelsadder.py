N= int(input("Enter a Nmmber: "))
for i in range (1,N+1):
    for j in range (1,N+2-i+2):
        if (j==1 or j==N+2-i+1):
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()