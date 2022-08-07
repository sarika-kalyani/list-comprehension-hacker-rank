x = int(input("num:"))#1
y = int(input("num:"))#1
z = int(input("num:"))#2
n = int(input("num:"))#3
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k!=n)))
