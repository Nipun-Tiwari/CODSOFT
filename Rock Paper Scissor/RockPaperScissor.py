from tkinter import *
import random
import tkinter.messagebox as tmsg
from custom_button import create_custom_button1,create_custom_button2
from PIL import Image, ImageTk
    
def win_close():
    root.destroy()
    game_screen()
def game_screen():
    pics = ["palm","fist","scissors"]
    img_list2=[]
    def game_logic(x):
        cpu=random.choice(pics)        
        original2 = Image.open(f"{cpu}.png")
        resized_img2 = original2.resize((250, 250), Image.HAMMING)
        img2 = ImageTk.PhotoImage(resized_img2)
        img_list2.append(img2)
        Label(root2, image=img2, bg="#b510da").pack()

        if(cpu==x):
            choice=tmsg.askyesno("Tie", "Match Draw\nDo you want to play again?")
        elif(x=="fist"):
            if(cpu=="palm"):
                choice=tmsg.askyesno("Lost", "You Lose\nDo you want to play again?")
            else:
                choice=tmsg.askyesno("Won", "You Won\nDo you want to play again?")
        elif(x=="palm"):
            if(cpu=="scissors"):
                choice=tmsg.askyesno("Lost", "You Lose\nDo you want to play again?")
            else:
                choice=tmsg.askyesno("Won", "You Won\nDo you want to play again?")
        elif(x=="scissors"):
            if(cpu=="fist"):
                choice=tmsg.askyesno("Lost", "You Lose\nDo you want to play again?")
            else:
                choice=tmsg.askyesno("Won", "You Won\nDo you want to play again?")
        if(choice):
            root2.destroy()
            game_screen()
        else:
            root2.destroy()
        
    root2 = Tk()
    root2.title("Rock Paper Scissors")
    root2.wm_iconbitmap("rock-paper-scissors.ico")
    root2.geometry("700x500")
    root2.config(bg="#b525da")
    root2.minsize(700,500)
    root2.maxsize(700,500)
    # Create a label at the top
    label1 = Label(root2, text="Your Pick:", font="Helvetica  30 bold italic",bg="#b525da")
    label1.pack(pady=15)

    # Create a frame for the buttons
    button_frame= Frame(root2,bg="#b525da")
    button_frame.pack()

    # # Create three buttons side by side
    # button1 = tk.Button(button_frame, text="Button 1")
    # button2 = tk.Button(button_frame, text="Button 2")
    # button3 = tk.Button(button_frame, text="Button 3")

    button1=create_custom_button1(button_frame,"Rock", lambda: game_logic('fist'))
    button2=create_custom_button1(button_frame,"Paper", lambda: game_logic('palm'))
    button3=create_custom_button1(button_frame,"Scissors", lambda: game_logic('scissors'))
    button1.pack(side=LEFT, padx=10)
    button2.pack(side=LEFT, padx=10)
    button3.pack(side=LEFT, padx=10)

    # Create another label below the buttons
    label2 = Label(root2, text="CPU picked:",font="Helvetica  30 bold italic",bg="#b525da")
    label2.pack(pady=(20,0))

    # Start the tkinter main loop
    root2.mainloop()

root = Tk()
root.geometry("700x500")
root.title("Rock Paper Scissors")
root.wm_iconbitmap("rock-paper-scissors.ico")
root.minsize(700,500)
root.maxsize(700,500)


f1 = Frame(root, width=650, height=490, bg="#ac538c", borderwidth=10, relief=SUNKEN)
f1.grid_propagate(False)  # Disable resizing of the Frame
f1.grid(row=0, column=0,padx=25)  # Use grid instead of pack


#Images
pics = ["palm","fist", "scissors"]
grids = [1, 2, 3]
rotate=[45,0,45]
image_list = []

for i,j,k in zip(pics, grids,rotate):
    original = Image.open(f"{i}.png")
    originalRot=original.rotate(k)
    resized_img = originalRot.resize((110, 110), Image.HAMMING)
    img = ImageTk.PhotoImage(resized_img)
    
    image_list.append(img)
    
    Label(f1, image=img, bg="#ac538c").grid(row=1, column=j,padx=50,pady=30)
    print(i, j)
b1=create_custom_button2(f1,"Play Game", command=win_close)
f1.pack_propagate(False)
b1.pack(side="top", pady=(220, 0))
b2=create_custom_button1(f1,"Quit",command=quit)
b2.pack(side="top", pady=(50, 0))

root.mainloop()
