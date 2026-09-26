"""
In this file , we will implement a set data structure .
we cna use out of the box available  set data structure in python as well if possible.
"""
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(5)
print('printing my set',myset)
print('trying to add duplicate now')
try:
    # This will not throw error . it will just return None
    print('adding 1 to myset',myset.add(1)) 
except Exception as e:
    print('Error:', e)
print('printing my set after trying to add duplicate',myset)