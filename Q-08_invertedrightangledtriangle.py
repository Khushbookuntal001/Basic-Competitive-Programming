M = int(input("Enter a number:"))
for i in range(M,0,-1):
    for j in range(M-i):
        print("_", end=" ") 
    for j in range(i):
        print("*", end=" ")
    print()