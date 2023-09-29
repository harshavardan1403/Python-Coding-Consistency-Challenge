print("\n\tProgram to print a Right-Angled hollow triangle with inverted number boundary")
n=int(input("\nEnter the number representing the height of the Hollow right angle triangle:"))
for i in range(0,n): #Loop corresponding to each row
    #Declaring the elements of each row of the triangle
    rowstr=""           #identifier representing the row
    front=""            #identifier representing the space before number
    middle=""           #identifier representing hollow spaces
    if i==0:        
        rowstr+="  "+("   "*(n-1))+"1"
    elif i==n-1:
        for j in range(n,1,-1):
            rowstr+=str(j)+" "
        rowstr+=" 1"
    else:
        front+="  "+"   "*(n-i-1)
        middle+="   "*(i-1)
        rowstr+=front+str(i+1)+middle+" 1"
    print(rowstr)
