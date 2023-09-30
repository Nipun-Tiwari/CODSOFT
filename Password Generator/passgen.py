from tkinter import *
import random

def passGenerator(n):
    alreadyUsed=[]
    def capAlpha():
        return random.randint(65,90)
    def smallAlpha():
        return random.randint(97,122)
    def numbers():
        return random.randint(48,57)
    def special():
        special_ascii=[33,35,36,37,38,64,42]
        return random.choice(special_ascii)
    password=""
    for i in range (0,n):
        char=random.randint(0,3)
        if(char==0):
            alreadyUsed.append(capAlpha)
            password+=chr(capAlpha())
        elif(char==1):
            alreadyUsed.append(smallAlpha)
            password+=chr(smallAlpha())
        elif(char==2):
            alreadyUsed.append(numbers)
            password+=chr(numbers())
        else:
            alreadyUsed.append(special)
            password+=chr(special())
    if(n>=6):
        for i in [capAlpha,smallAlpha,numbers,special]:
            if(i not in alreadyUsed):
                password+=chr(i())
    passVar.set(password)

root=Tk()
root.title("Password Generator")
root.geometry("650x300")
root.minsize(650,300)
root.maxsize(650,300)
nVal=IntVar()
passVar=StringVar()
f=Frame(root,border=5,width=490,height=390,pady=20)
Label(f,text="Enter the length:",font="Arial 22").grid(row=0,column=0,padx=(0,10))
Entry(f,textvariable=nVal,font="Arial 22",width=5).grid(row=0,column=1,padx=(100,20))
Button(f,text="Confirm", font="Arial 17",bg="red",command= lambda: passGenerator(nVal.get())).grid(row=0,column=2,padx=(20,5))

f.pack(side="top",anchor="w")
Label(root,text="Generated Password:",font="Arial 22").pack(side="left",anchor="sw",pady=50,padx=5)
Entry(root,textvariable=passVar,font="Arial 22").pack(side="left",anchor="sw",pady=50,padx=(8,0))



root.mainloop()