from tkinter import *

root = Tk()
root.geometry("700x500")
root.configure(bg="black")
root.title("Simple Calculator")
root.wm_iconbitmap("Calculatoricon.ico")
root.minsize(700,500)
root.maxsize(700,500)
f1 = Frame(root, width=700, height=100, bg="#1d3849")
f1.pack()

f2 = Frame(root, width=550, height=400, bg="#205b7a")
f2.pack(side="left")

f3 = Frame(root, width=150, height=400, bg="#a2bbcf")
f3.pack(side="left", padx=3, pady=3)

# Initialize the input variable
strVal = StringVar()
strVal.set("")

def addStr(x):
    current_value = strVal.get()
    strVal.set(current_value + x)

def delStr():
    current_value = strVal.get()
    strVal.set(current_value[:-1])

def delAll():
    strVal.set("")

def calculate_result():
    curVal = strVal.get()
    try:
        result = eval(curVal)
        strVal.set(result)
    except Exception as e:
        strVal.set("Error")

# Frame 2: Keypad
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.'
]

row_val = 0
col_val = 0

for button in buttons:
    Button(f2, text=button, padx=22, pady=7, font=("Arial", 20), width=5, height=1, fg="white", bg="#7A3F20",
           relief=RAISED, borderwidth=7, command=lambda b=button: addStr(b)).grid(row=row_val, column=col_val, padx=20, pady=10)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# frame 3: Operations
padX = 3
padY = 16
padBX = 6
padBY = 3
Button(f3, text="+", command=lambda: addStr('+'), font="arial 20", bg="#CFB6A2", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=0, column=0, padx=padX, pady=padY)
Button(f3, text="-", command=lambda: addStr('-'), font="arial 20", bg="#CFB6A2", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=0, column=1, padx=padX, pady=padY)
Button(f3, text="*", command=lambda: addStr('*'), font="arial 20", bg="#CFB6A2", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=1, column=0, padx=padX, pady=padY)
Button(f3, text="/", command=lambda: addStr('/'), font="arial 20", bg="#CFB6A2", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=1, column=1, padx=padX, pady=padY)
Button(f3, text="C", command=delStr, font="arial 20", bg="#CFB6A2", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=2, column=0, padx=padX, pady=padY)
Button(f3, text="CE", command=delAll, font="arial 20", bg="red", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=2, column=1, padx=padX, pady=padY)
Button(f3, text="=", command=calculate_result, font="arial 20", bg="#43ed12", relief=RAISED, borderwidth=5,
       padx=padBX, pady=padBY).grid(row=3, column=0, padx=padX, pady=padY)

# frame 1: Screen
Entry(f1, textvariable=strVal, font=("mooli", 36), bg="black", fg="white", bd=0, insertwidth=4, width=15,
      justify="right").pack()

root.mainloop()
