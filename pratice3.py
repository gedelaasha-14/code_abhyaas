
'''
#1) finding missing number in an array

n=int(input("enter no. of elements:"))
l=[1,4,3] #the list elements within the range only we can enter n-1 elements only
asum=(n*(n+1))//2
sum=0
for i in l:
	sum+=i
mis=asum-sum
print(mis) '''


'''
# 2)to find peak element which is greater than its neighbour elements

list=[5,80,20,15]
l=len(list)
if list[0]>=list[1]:
	print(list[0])
for i in range(1,l):
	if(list[i]>=list[i-1] and list[i]>=list[i+1]):
		print(list[i])
if list[-1]>=list[-2]:
	print(list[-1])'''
 

'''# 3) left rotate of an array
list=[1,2,3,4,5]
k=int(input("enter no. of rotates:"))
l=len(list) 
for i in range(0,k):  # for left rotation 
	temp=list[0]  
	for j in range(0,l-1):
		list[j]=list[j+1]
	list[l-1]=temp 
for i in range(0,k): # for right rotation
	temp=list[l-1]
	for j in range(l-1,0,-1):
		list[j]=list[j-1]
	list[0]=temp
	 
print(list)'''


# 4)to fid kth largest and smallest in an array
list=[1,6,3,4,5,2]
k=int(input("enter kth number:"))
list=sorted(list)
s=list[k-1]
print(s)
l=list[k]
print(l)


