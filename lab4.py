import array as k
y=k.array('d', [8,3,1,2,9,5,11]) 
print('here is the array elements'‚y) 
print('the item size is' ‚y.itemsize)
print(y.itemsize*len(y))
j= k.array('d', [1,2,3,4,5,6]) 
s=j.tobytes()
print(s)