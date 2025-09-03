M = int(input("Enter a number:"))
for i in range(1, M+1):
    for j in range(M-i):
        print("_", end=" ") 
    for j in range(i):
        print("*", end=" ")
    print()