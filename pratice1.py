'''
   # 1) to find largest element in a given array
list=[20,16,36,14,30]
max=-9999
for i in list:
	if i>max:
		max=i
print(max)   '''



'''   # 2)to find frequency of given element in an array
list=[12,4,8,4,6,4]
count=0
k=int(input("enter element:"))
for i in list:
	if i==k:
		count+=1
print(count)  '''

'''
 # 3) rearrange the string according to given indices
str="ahpyp"
indices=[1,0,2,4,3]
l=len(indices)
res=['']*len(str)
for i in range(0,l):
	res[indices[i]]=str[i]
res=''.join(res)
print(res)  '''
 
  # 4)to move all zeros in an array to end 
list=[9,0,3,4,0,0,1,0]
res=[]
for i in list:
	if i!=0:
		res.append(i)
for i in list:
	if i==0:
		res.append(i)
print(res)


 
