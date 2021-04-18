from tkinter import *
def binary2gray(bininput):
    #bininput=int(input("Enter binary number:"),2)
    #print(len(str(bin(bininput))))
    s=str(bin(bininput))
    #print(s)
    res=""
    for i in range(3,len(str(bin(bininput)))):
        dig=int(str(bin(bininput))[i])+int(str(bin(bininput))[i-1])
        #s=int(s)+int(dig)
        if dig%2==0:
            dig=0
        else:
            dig=1
        #print(dig)
        res=res+str(dig)[0]
    graycode=str(bin(bininput))[2]+str(res)
    print(graycode)
    resLbl=Label(text=" "*100)
    resLbl.grid(row=7,column=2,columnspan=600)
    resLbl=Label(text="Gray Code representing binary number "+str(bin(bininput))+" is "+ str(graycode),font="Helvetica 14 bold",fg="green")
    resLbl.grid(row=7,column=2,columnspan=600)
def gray2binary(grayinput):
    #grayinput=int(input("Enter Gray code:"),2)
    #print(len(str(bin(grayinput))))
    s=str(bin(grayinput))[2]
    res=""
    for i in range(3,len(str(bin(grayinput)))):
        dig=str(bin(grayinput))[i]
        s=int(s)+int(dig)
        if s%2==0:
            s=0
        else:
            s=1
        #print(s)
        res=res+str(s)[0]
    binary=str(bin(grayinput))[2]+str(res)
    print(binary)
    resLbl=Label(text=" "*100)
    resLbl.grid(row=7,column=2,columnspan=600)
    resLbl=Label(text="Binary Number representing Gray Code "+str(bin(grayinput))+" is "+ str(binary),font="Helvetica 14 bold",fg="blue")
    resLbl.grid(row=7,column=2,columnspan=600)
def createwidgets():
    headLbl=Label(text="Convert from Gray Code to binary and Binary to Gray code",font="Verdana 13 bold",fg="red")
    headLbl.grid(row=0,column=0,columnspan=600)
    cmtLbl=Label(text="Enter only ones or zeros in Text Box").grid(row=1,column=0,columnspan=600)
    inpt=Text(width=60,height=1)
    inpt.grid(row=3,column=0,columnspan=600)
    bin2grayBtn=Button(text="Convert Binary to Gray Code",command=lambda:binary2gray(int(inpt.get(0.0,"end-1c"),2)))
    bin2grayBtn.grid(row=5,column=80)
    gray2binBtn=Button(text="Convert Gray Code to Binary",command=lambda:gray2binary(int(inpt.get(0.0,"end-1c"),2)))
    gray2binBtn.grid(row=5,column=160)
    #print(inpt.get(0.0,"end-1c"))
    pass
def main():
    root=Tk()
    createwidgets()
    root.geometry("600x180")
    root.mainloop()
main()

