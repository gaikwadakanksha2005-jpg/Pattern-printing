n = 5
# Upper part
for i in range(1, n+1): #Uesd for rows
    for j in range(i): #manage left side stars
        print("*", end=" ")
    for j in range(2*(n-i)): #Increase stars by 2
        print(" ", end=" ") #for space
    for j in range(i):
        print("*", end=" ") #print stars
    print()
# Lower part
for i in range(n-1, 0, -1): #For reverse
    for j in range(i):
        print("*", end=" ") #print stars
    for j in range(2*(n-i)):#increase by 2 in each line
        print(" ", end=" ") #for empty space
    for j in range(i): 
        print("*", end=" ") #print stars
    print()