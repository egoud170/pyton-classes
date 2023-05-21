"""In this looping statements hear  'L' acts as a variable 
for values present in List and 'Z' is replica of 'L'.
L values goes into Z""" 
#For LoopEx1:
L=[1,2,3,4]
for z in L:
    if z==1: 
        print("1")
        break
    else:
        print("0")
#Ex2:
l=[1,2,3,4,5]
sum=0

for i in l:
    sum=sum+i
    print(sum)

#Ex:3:For loop in range

for i in range(1,10,2):
  print(i) 
#Ex:while
c=0
while c<3:
    c=c+1
    print("while") 
else:
    print("op")      