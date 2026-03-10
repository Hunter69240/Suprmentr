
#Continuous sum but enter 0 to break
sum=0
while True:
    a=int(input("Enter number to add , enter 0 to stop:"))
    if a==0:
        break
    else:
        sum+=a
print("Final sum is",sum)