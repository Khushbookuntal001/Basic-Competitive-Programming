num=int(input("enter a number: "))
if num%3==0 or num%10==4:
    print("divisible by 3 and last digit is 4")
else:
    print("not divisible by 3 and last digit is not 4")