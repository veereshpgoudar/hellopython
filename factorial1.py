n=int(input("Enter a number:")) 
temp=n 
fact=1 
while n!=0: 
 fact*=n 
 n-=1 
print("Factorial of {0} is {1}".format(temp,fact))