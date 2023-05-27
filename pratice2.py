'''
  # 1)  reverse of an array
list=[1,2,3,4,5]
list=list[::-1]
print(list)   '''

'''
#  2)remove even integers from an array
list=[3,2,4,5,7,10,12]
res=[]
for i in list:
	if i%2!=0:
		res.append(i)
print(res)  '''

'''
 # 3)second largest element in an array
list=[3,2,4,5,7,10,12]
max1=-9999
for i in list:
	if i>max1:
		max1=i
max2=-9999
for i in list:
	if i>max2 and i!=max1:
		max2=i
print(max2)   '''


# 4) to convert an array size 5 to array size 8
list=[1,2,3,4,5]
res=[0]*8
for i in range(0,len(list)):
	res[i]=list[i]
print(res)

