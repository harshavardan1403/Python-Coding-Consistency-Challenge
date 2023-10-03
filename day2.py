m=int(input())
n=int(input())
lastnum=n
for i in range(0,m):
    rowstr=""
    if i==0:
        for j in range(1,n+1):
            rowstr+=str(j)+" "
    elif i==m-1:
        for j in range(n*m-n+1,n*m+1):
            rowstr+=str(j)+" "
    else:
        rowstr=str(lastnum+1)+" "+("  "*(n-2))+str(lastnum+n)
        lastnum=lastnum+n
    print(rowstr)
