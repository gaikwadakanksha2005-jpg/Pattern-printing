n=5
for i in range(1,n+1): #for rows
    for j in range(1,n-i+1): 
        print(" ",end=" ")#for space
    for k in range(1,i*2): #increse by 2 in each line
        print("*",end=" ") # print stars in same line
    print()   

for i in range(n-1,0,-1): #for reverse
    for j in range(1,n-i+1): # for space
        print(" ",end=" ")#print space
    for k in range(1,i*2):  #increse by 2 in each line
        print("*",end=" ")# print stars in same line
    print()         
