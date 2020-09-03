import numpy as np

print(np.__version__,'\n')

#numpy array- collection same data typed values

#creating numpy array from list
lst=[1,2,3,4,5]
arr=np.array(lst)
print('\n',arr)

#vectorized operations-apply operations to the whole array
print('\n',arr+2)

print('\n',arr*4)

print('\n',arr/2)

print('\n',arr//2)

#creation of arrays of zeroes and ones
print('\n',np.zeros((2,2)))

print('\n',np.ones((2,2)))

#merging 2 arrays
arr1=np.matrix([1,2,3])
arr2=np.matrix([4,5,6])

print('\n Horizontal append',np.hstack((arr1,arr2)))

print('\n Vertical append',np.vstack((arr1,arr2)))

#creating 2d arrays from list
lst1=[[1,2,3],[4,5,6],[7,8,9]]
arr2d=np.array(lst1)
print('\n',arr2d)

#arrays of a particular type
arr2d=np.array(lst1,dtype='float')
print('\n',arr2d)

#converting data type of array
print('\n',arr2d.astype('int').astype('str'))

#creating boolean array
arr2db=np.array([1,0,0,5,0,0],dtype='bool')
print('\n',arr2db)

#array consisting of various element types
arr2dobj=np.array(['1','ML'],dtype=object)
print('\n',arr2dobj)

#converting array back to list
lst_conv=arr2dobj.tolist()
print('\n',lst_conv)

#shape function
print('\n',arr2d.shape)

print('\n',arr2d.size)

print('\n',arr2d.dtype)

print('\n',arr2d.ndim)

#slicing
print('\n',arr2d[:2,:2])

#creating boolean matrix on applying condtional expression
bool_matrix=arr2d>4
print('\n',bool_matrix)

#reversing an array
print('\n',arr2d[::-1])

#inserting nan(not a number) and inf(infinity)
arr2d[1,2]=np.nan
print('\n',arr2d)

arr2d[2,2]=np.inf
print('\n',arr2d)

#replacing missing values with -1

mv=np.isnan(arr2d)
print('\n',mv)
arr2d[mv]=-1
print('\n',arr2d)

#max, min, mean
lst1=[[1,2,3],[4,5,6],[7,8,9]]
arr2d=np.array(lst1)

print('\n',arr2d.mean())

print('\n',arr2d.max())

print('\n',arr2d.min())

#row and column wise min max mean
print('\n',np.amin(arr2d,axis=0))

print('\n',np.amax(arr2d,axis=0))

print('\n',np.amin(arr2d,axis=1))

print('\n',np.amax(arr2d,axis=1))

#assigning a portion of an array to other
arrn=arr2d[:2,:2]
print('\n',arrn)

#its like an alias so 22 will be reflected in the parent array as well
arrn[:1,:1]=22
print('\n',arr2d)


#assigning a portion by copying
arrn=arr2d[:2,:2].copy()
print('\n',arrn)

arrn[:1,:1]=76
#this time it wont reflect in parent array as it is a copy
print('\n',arr2d)
print('\n',arrn)

#reshaping arrays
arrs=np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8]])
print('\n',arrs)
print('\n',arrs.reshape(2,6))

#flatten arrs to 1d
print('\n',arrs.flatten())
#no change in parent array even if we change the flattened array

#changing raveled array changes parent array
print('\n',arrs.ravel())

#random numbers generation

#prints numbers between 0 and 1
print('\n',np.random.rand(3,3))

#printsnormal distribution with mean=0 and variance =1
print('\n',np.random.randn(3,3))

#prints a random number between 0 and 1
print('\n',np.random.random())

#prints random number between 0 ans 1 of size (2,2)
print('\n',np.random.random(size=[2,2]))

#prints random number between 0 and 10
print('\n',np.random.randint(0,10,size=[2,2]))

randele=np.random.randint(0,5,size=[10])
print('\n',randele)

#unique elements and their count
uniq,count=np.unique(randele,return_counts=True)
print('\n unique items',uniq)
print('\n counts',count)

lst=np.random.choice(['n','u','m','p','y'],size=15)
print('\n', lst)

uniq1,count=np.unique(lst,return_counts=True)
print('\n unique items',uniq1)
print('\n counts',count)



