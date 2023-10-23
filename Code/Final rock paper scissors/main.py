from tkinter import *
from PIL import Image, ImageTk
import random
root=Tk()
root.title("Rock Paper Scissors By Shadik")
root.geometry('1100x400')
def new_game():
    global yourchoice
    global pcchoice
    global status
    global yscore
    global pcscore
    global round_no
    global brock
    global bpaper
    global bscissors
    global winner
    global youlabel
    global pclabel
    global round_count
    global roun
    global anouns

    yscore.set("0")
    pcscore.set("0")
    round_no.set("0")
    brock = Button(root, image=rock, command=callrock)
    bpaper = Button(root, image=paper, command=callpaper)
    bscissors = Button(root, image=scissors, command=callsci)
    brock.grid(row=5, column=4)
    bpaper.grid(row=5, column=5)
    bscissors.grid(row=5, column=6)
    vs=Label(root,image=white)
    vs.grid(row=2,column=5)
    new = Button(root, text="NEW GAME", font=15, command=new_game, state="disabled")
    new.grid(row=5, column=8)
    status.set("Let's Play Again")


def callrock():
    global yourchoice
    global pcchoice
    global status
    global yscore
    global pcscore
    global round_no
    global brock
    global bpaper
    global bscissors
    global winner
    global youlabel
    global pclabel
    global round_count
    global roun
    global anouns
    rn = int(round_no.get()) + 1
    round_no.set(str(rn))

    if rn<=9:

        yourchoice.grid_forget()
        pcchoice.grid_forget()
        computer_choice = random.choice(computer)
        yourchoice = Label(root, image=rock)
        pcchoice = Label(root, image=computer_choice)
        if computer_choice == rock:
            status.set("It's A Tie")
        elif computer_choice == paper:
            status.set("Alas...Better Luck Next Round")
            pcpoint=int(pcscore.get())+1
            pcscore.set(str(pcpoint))
        elif computer_choice == scissors:
            status.set("Congo....You Won!!!")
            youpoint = int(yscore.get())+1
            yscore.set(str(youpoint))
        yourchoice.grid(row=2, column=2)
        pcchoice.grid(row=2, column=8)
    else:
        computer_choice = random.choice(computer)
        yourchoice = Label(root, image=rock)
        pcchoice = Label(root, image=computer_choice)
        yourchoice.grid(row=2, column=2)
        pcchoice.grid(row=2, column=8)
        if computer_choice == paper:

            pcpoint = int(pcscore.get()) + 1
            pcscore.set(str(pcpoint))


        elif computer_choice == scissors:
            youpoint = int(yscore.get()) + 1
            yscore.set(str(youpoint))
        a = int(yscore.get())
        b = int(pcscore.get())
        brock = Button(root, image=rock, command=callrock, state="disabled")
        bpaper = Button(root, image=paper, command=callpaper, state="disabled")
        bscissors = Button(root, image=scissors, command=callsci, state="disabled")
        new = Button(root, text="NEW GAME", font=15, command=new_game)
        new.grid(row=5, column=8)

        brock.grid(row=5, column=4)
        bpaper.grid(row=5, column=5)
        bscissors.grid(row=5, column=6)
        if a > b:
            Label(root, image=win).grid(row=2, column=5)
            status.set("Congo....You Won!!!")
        elif b > a:
            Label(root, image=lose).grid(row=2, column=5)
            status.set("You Lost!!!")
        else:
            Label(root, image=draw).grid(row=2, column=5)
            status.set("It's a Tie")


def callpaper():
    global yourchoice
    global pcchoice
    global winner
    global yscore
    global pcscore
    global round_no
    global brock
    global bpaper
    global bscissors
    global winner
    global youlabel
    global pclabel
    global round_count
    global roun
    global anouns
    rn = int(round_no.get()) + 1
    round_no.set(str(rn))

    if rn <= 9:
        yourchoice.grid_forget()
        pcchoice.grid_forget()
        computer_choice = random.choice(computer)
        yourchoice = Label(root, image=paper)
        pcchoice = Label(root, image=computer_choice)
        if computer_choice == rock:
            status.set("Congo...You Won")
            youpoint = int(yscore.get()) + 1
            yscore.set(str(youpoint))
        elif computer_choice == paper:
            status.set("It's A Tie")
        elif computer_choice == scissors:
            status.set("Alas...Better Luck Next Round")
            pcpoint = int(pcscore.get()) + 1
            pcscore.set(str(pcpoint))
        yourchoice.grid(row=2, column=2)
        pcchoice.grid(row=2, column=8)
    else:
        computer_choice = random.choice(computer)
        yourchoice = Label(root, image=paper)
        pcchoice = Label(root, image=computer_choice)
        yourchoice.grid(row=2, column=2)
        pcchoice.grid(row=2, column=8)

        if computer_choice == scissors:

            pcpoint = int(pcscore.get()) + 1
            pcscore.set(str(pcpoint))


        elif computer_choice == rock:
            youpoint = int(yscore.get()) + 1
            yscore.set(str(youpoint))
        a = int(yscore.get())
        b = int(pcscore.get())
        brock = Button(root, image=rock, command=callrock, state="disabled")
        bpaper = Button(root, image=paper, command=callpaper, state="disabled")
        bscissors = Button(root, image=scissors, command=callsci, state="disabled")
        new = Button(root, text="NEW GAME", font=15, command=new_game)
        new.grid(row=5, column=8)

        brock.grid(row=5, column=4)
        bpaper.grid(row=5, column=5)
        bscissors.grid(row=5, column=6)
        if a > b:
            Label(root, image=win).grid(row=2, column=5)
            status.set("Congo....You Won!!!")

        elif b > a:
            Label(root, image=lose).grid(row=2, column=5)
            status.set("You Lost!!!")

        else:
            Label(root, image=draw).grid(row=2, column=5)
            status.set("It's A Tie")


def callsci():
    global yourchoice
    global pcchoice
    global winner
    global yscore
    global pcscore
    global round_no
    global brock
    global bpaper
    global bscissors
    global winner
    global youlabel
    global pclabel
    global round_count
    global roun
    global anouns

    rn = int(round_no.get()) + 1
    round_no.set(str(rn))

    if rn <= 9:
        yourchoice.grid_forget()
        pcchoice.grid_forget()
        computer_choice = random.choice(computer)
        yourchoice = Label(root, image=scissors)
        pcchoice = Label(root, image=computer_choice)
        if computer_choice == paper:
            status.set("Congo...You Won")
            youpoint = int(yscore.get()) + 1
            yscore.set(str(youpoint))
        elif computer_choice == scissors:
            status.set("It's A Tie")
        elif computer_choice == rock:
            status.set("Alas...Better Luck Next Round")
            pcpoint = int(pcscore.get()) + 1
            pcscore.set(str(pcpoint))

        yourchoice.grid(row=2, column=2)
        pcchoice.grid(row=2, column=8)
    else:
        computer_choice = random.choice(computer)
        yourchoice = Label(root, image=scissors)
        pcchoice = Label(root, image=computer_choice)
        yourchoice.grid(row=2, column=2)
        pcchoice.grid(row=2, column=8)

        if computer_choice == rock:

            pcpoint = int(pcscore.get()) + 1
            pcscore.set(str(pcpoint))


        elif computer_choice == paper:
            youpoint = int(yscore.get()) + 1
            yscore.set(str(youpoint))
        a = int(yscore.get())
        b = int(pcscore.get())
        brock = Button(root, image=rock, command=callrock, state="disabled")
        bpaper = Button(root, image=paper, command=callpaper, state="disabled")
        bscissors = Button(root, image=scissors, command=callsci, state="disabled")
        new = Button(root, text="NEW GAME", font=15, command=new_game)
        new.grid(row=5, column=8)

        brock.grid(row=5, column=4)
        bpaper.grid(row=5, column=5)
        bscissors.grid(row=5, column=6)
        if a > b:
            Label(root, image=win).grid(row=2, column=5)
            status.set("Congo....You Won!!!")

        elif b > a:
            Label(root, image=lose).grid(row=2, column=5)
            status.set("You Lost!!!")

        else:
            Label(root, image=draw).grid(row=2, column=5)
            status.set("It's A Tie")


rockimg = Image.open("rock - Copy.png")
paperimg = Image.open("paper - Copy.png")
sciimg = Image.open("scissors - Copy.png")
userimg = Image.open("user - Copy.png")
robotimg = Image.open("computer - Copy.png")
winimg = Image.open("won.webp")
lostimg = Image.open("loose.png")
whiteimg = Image.open("lets play.png")
drawimg = Image.open("draw.jpg")
resized_draw = drawimg.resize((200,150))
resized_win = winimg.resize((200,150))
resized_lost=lostimg.resize((200,150))
reswht = whiteimg.resize((200,150))
resized_rock = rockimg.resize((100,100))
resizzed_paper = paperimg.resize((100,100))
resizzed_sci= sciimg.resize((100,100))
resized_user = userimg.resize((100,100))
resized_robot = robotimg.resize((100,100))
draw = ImageTk.PhotoImage(resized_draw)
rock = ImageTk.PhotoImage(resized_rock)
paper = ImageTk.PhotoImage(resizzed_paper)
scissors = ImageTk.PhotoImage(resizzed_sci)
user = ImageTk.PhotoImage(resized_user)
robot = ImageTk.PhotoImage(resized_robot)
win = ImageTk.PhotoImage(resized_win)
lose = ImageTk.PhotoImage(resized_lost)
white = ImageTk.PhotoImage(reswht)
computer = [rock, paper, scissors]

y = Label(root,text="Your score ",font=15)
p = Label(root,text="Computers Score",font=15)
vs = Label(root,image=white)
vs.grid(row=2,column=5)
y.grid(row=0,column=0)
p.grid(row=0,column=6)
yscore = StringVar()
yscore.set("0")
pcscore = StringVar()
pcscore.set("0")
youscreen=Entry(root,textvariable=yscore,font=20)
pcscreen=Entry(root,textvariable=pcscore,font=20)
youscreen.grid(row=0,column=2)
pcscreen.grid(row=0,column=8)

youlabel = Label(root,text="Your Choice",font="align 15")
pclabel = Label(root,text="Computers Choice",font="align 15")

youlabel.grid(row=1,column=2)
pclabel.grid(row=1,column=8)

yourchoice = Label(root,image=user)
pcchoice = Label(root,image=robot)

yourchoice.grid(row=2,column=2)
pcchoice.grid(row=2,column=8)
status = StringVar()
status.set("Lets's Start")
winner = Label(root,textvariable=status,font=30)
winner.grid(row=3,column=4,columnspan=4)








brock = Button(root,image=rock,command=callrock)
bpaper = Button(root,image=paper,command=callpaper)
bscissors = Button(root,image=scissors,command=callsci)
new = Button(root, text="NEW GAME", font=15, command=new_game, state="disabled")
new.grid(row=5, column=8)

brock.grid(row=5,column=4)
bpaper.grid(row=5,column=5)
bscissors.grid(row=5,column=6)

roun = Label(root,text="Round No",font=20)

round_no = StringVar()
round_no.set("0")
round_count = Entry(root,textvariable=round_no,font=20)

round_count.grid(row=6,column=5)


roun.grid(row=6,column=4)
anouns = Label(root,text="There will be 10 rounds total",font=15)
anouns.grid(row=7,column=3,columnspan=5)




root.mainloop()