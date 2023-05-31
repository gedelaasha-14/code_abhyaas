'''  
# to check given string is palindrome or not

str=input("enter str:")
temp=str[::-1]
if str==temp:
	print("palindrome")
else:
	print("not")  '''
	
'''
#to check given number is perfect or not

n=int(input("enter number:"))
sum=0
temp=n
for i in range(1,n):
	if n%i==0:
		sum+=i
if sum==temp:
	print("perfect")
else:
	print("not perfect") '''


'''	
# Program to generate Fibonacci series up to a given number of terms.

n=int(input("enter n:"))
a=0
b=1
c=a+b
res=[]
for i in range(0,n):
	res.append(a)
	a=b
	b=c
	c=a+b
print(res)  '''


'''
#Program to find whether given number is an Armstrong number or not.
n=int(input("enter number:"))
rev=0
l=0
temp=n
while(n!=0):
	l+=1
	n//=10
n=temp
while n!=0:
	k=n%10
	rev+=pow(k,l)
	n//=10
if temp==rev:
	print("armstrong")
else:
	print("not") '''

# Program to find given number is a strong number or not.

n=int(input("enter n:"))
sum=0
temp=n

while(n!=0):
	fact=1
	k=n%10
	for i in range(1,k+1):
		fact*=i
	#print(fact)
	sum+=fact
	n//=10
if sum==temp:
	print("strong number")
else:
	print("not")
	
