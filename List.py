#List
"""List is a data type which we can store different types of values
which begins and ends with []"""
#Ex:append it exsctly takes one argument
L=[1,2,'jai',0]
L.append(1)
print(L)
#Ex:Extend in this it added in (last)
L.extend([1,2,3])
print(L)
#EX:insert in this  here we can specify index  and add  variables
L.insert(2,'in')
print(L)
#Ex:Count in this true considered as 1 and false is 0
print(L.count(1))
#Ex:len operation explains  that length  of  the values present in variable
print(len(L))
#Ex:pop here pop=Delete it is pops the given index value
L.pop(2)
print(L)
#Ex:Reverse here reverse reprents it print vlaues reverse
L.reverse()
print(L)
#Ex:sort here by using  sort it print values  in variable small to bigger it is only applicable  for numbers
n=[1,22,1000,0,34,2,3]
n.sort()
print(n)

L=[1,2,'jai',2,0]
L.remove(2)
print(L)#here it removes first element. 

m=[1,22,1000,[0,34,2],3]
print(m[3][2])

L=[1,2,'jai',0]
v=L.copy
L.append(5)
print(L)
#Slicing  in list
m=[1,22,1000,[0,34,2],3]
print(m[5:]) #[5:] reprents  right side
print(m[:]) #[:5] represents Left side
            #[:] represents whole set of list.
            #[1:2:3] represents start and stop and skip
            #[1:2] here 1 is index,2 is element