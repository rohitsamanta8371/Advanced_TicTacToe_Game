import tkinter.messagebox
from tkinter import*
root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='VioletRed4')

Tops = Frame(root, bg='VioletRed4', pady=2,width=1350,height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle=Label(Tops, font=('arial',50,'bold'),text="Rohit's Tic Tac Toe Game", bd=21, bg='Maroon4', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root, bg='maroon3', bd=10,width=1350,height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bg='VioletRed1',bd=10, pady=2, padx=10,width=750,height=500, relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bg='maroon2',bd=10, pady=2,padx=10,width=560,height=500, relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bg='VioletRed3',bd=10, pady=2,padx=10,width=560,height=200, relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame, bg='VioletRed3',bd=10, pady=2,padx=10,width=560,height=200, relief=RIDGE)
RightFrame2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()
PlayerX.set(0)
PlayerO.set(0)

buttons=StringVar()
click=True
def checker(buttons):#execute X O one after another
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click=False
        scorekrper()
    elif buttons["text"]==" " and click==False:
        buttons["text"]="O"
        click=True
        scorekrper()
def scorekrper():#score generating
    # conditions for O
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="green2")
        button2.configure(background="green2")
        button3.configure(background="green2")
        n=float(PlayerO.get())#updating score
        score=(n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("O won","O won the game")
    if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        button4.configure(background="green2")
        button5.configure(background="green2")
        button6.configure(background="green2")
        n = float(PlayerO.get())  # updating score
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("O won", "O won the game")
    if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        button7.configure(background="green2")
        button8.configure(background="green2")
        button9.configure(background="green2")
        n = float(PlayerO.get())  # updating score
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("O won", "O won the game")
    if (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        button3.configure(background="green2")
        button5.configure(background="green2")
        button7.configure(background="green2")
        n = float(PlayerO.get())  # updating score
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        button1.configure(background="green2")
        button5.configure(background="green2")
        button9.configure(background="green2")
        n = float(PlayerO.get())  # updating score
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("O won", "O won the game")
    if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        button1.configure(background="green2")
        button4.configure(background="green2")
        button7.configure(background="green2")
        n = float(PlayerO.get())  # updating score
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("O won", "O won the game")
    if (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        button2.configure(background="green2")
        button5.configure(background="green2")
        button8.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("O won", "O won the game")
    if (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        button3.configure(background="green2")
        button6.configure(background="green2")
        button9.configure(background="green2")
        n = float(PlayerO.get())  # updating score
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("O won", "O won the game")

    #conditiom for X
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        button1.configure(background="green2")
        button2.configure(background="green2")
        button3.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background="green2")
        button5.configure(background="green2")
        button6.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        button7.configure(background="green2")
        button8.configure(background="green2")
        button9.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        button3.configure(background="green2")
        button5.configure(background="green2")
        button7.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        button1.configure(background="green2")
        button5.configure(background="green2")
        button9.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        button1.configure(background="green2")
        button4.configure(background="green2")
        button7.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        button2.configure(background="green2")
        button5.configure(background="green2")
        button8.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")
    if (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        button3.configure(background="green2")
        button6.configure(background="green2")
        button9.configure(background="green2")
        n = float(PlayerX.get())  # updating score
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("X won", "X won the game")

def reset():#only reset the arena not reset the score board
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="VioletRed2")
    button2.configure(background="VioletRed2")
    button3.configure(background="VioletRed2")
    button4.configure(background="VioletRed2")
    button5.configure(background="VioletRed2")
    button6.configure(background="VioletRed2")
    button7.configure(background="VioletRed2")
    button8.configure(background="VioletRed2")
    button9.configure(background="VioletRed2")
    #tkinter.messagebox.showinfo("both", "IF PLAYER A TAKEN THIS ATTEMPT THEN PLAYER B WILL ATTEMPT THIS FIRST")

def NewGame():#creating a new game, score is also reset
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

lblPlayerX=Label(RightFrame1, font=('arial',40,'bold'),text="Player A(X):", padx=2,pady=2,fg='Cornsilk', bg='VioletRed3')
lblPlayerX.grid(row=0,column=0,sticky=W)
txtPlayerX=Entry(RightFrame1,font=('arial',40,'bold'), bd=2, fg="VioletRed4", textvariable=PlayerX,width=14,justify=LEFT)
txtPlayerX.grid(row=0,column=1)

lblPlayerO=Label(RightFrame1, font=('arial',40,'bold'),text="Player B(O):", padx=2,pady=2,fg='Cornsilk', bg='VioletRed3')
lblPlayerO.grid(row=1,column=0,sticky=W)
txtPlayerO=Entry(RightFrame1,font=('arial',40,'bold'), bd=2, fg="VioletRed4", textvariable=PlayerO,width=14,justify=LEFT)
txtPlayerO.grid(row=1,column=1)

btnReset=Button(RightFrame2,text="Reset",font=('Times 26 bold'), height=3, width=15,bg='VioletRed3',command=reset)
btnReset.grid(row=1, column=0, sticky=S+N+E+W)
btnNewGame=Button(RightFrame2,text="New Game ",font=('Times 26 bold'), height=3, width=15,bg='VioletRed3',command=NewGame)
btnNewGame.grid(row=1, column=1, sticky=S+N+E+W)

button1=Button(LeftFrame,text=" ",font=('Times 26  bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9=Button(LeftFrame,text=" ",font=('Times 26 bold'), height=3, width=8,bg='VioletRed2',command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)
root.mainloop()
