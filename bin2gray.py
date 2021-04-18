bininput=int(input("Enter binary number:"),2)
print(len(str(bin(bininput))))
s=str(bin(bininput))
print(s)
res=""
for i in range(3,len(str(bin(bininput)))):
    dig=int(str(bin(bininput))[i])+int(str(bin(bininput))[i-1])
    #s=int(s)+int(dig)
    if dig%2==0:
        dig=0
    else:
        dig=1
    print(dig)
    res=res+str(dig)[0]
graycode=str(bin(bininput))[2]+str(res)
print(graycode)
