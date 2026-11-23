n=5
for i in range(1,n+1): #uesd for rows
    for j in range(1,i+1): #uesd for column
        if i==n or j==1 or j==i : #any condition true print it
            print("*",end=" ") #print stars
        else:
            print(" ",end=" ") #for spacing
    print()        