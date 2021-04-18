grayinput=int(input("Enter Gray code:"),2)
print(len(str(bin(grayinput))))
s=str(bin(grayinput))[2]
res=""
for i in range(3,len(str(bin(grayinput)))):
    dig=str(bin(grayinput))[i]
    s=int(s)+int(dig)
    if s%2==0:
        s=0
    else:
        s=1
    print(s)
    res=res+str(s)[0]
binary=str(bin(grayinput))[2]+str(res)
print(binary)
