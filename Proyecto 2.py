from tkinter import *
import tkinter as tk
import winsound
import random
import pickle
import os

#Global Data
namep = ""

#1###########################################################################################################
#Open_Window class: this opens the Game_Win class and the Home_Window class.

class Open_Window:

    #This function sends Home_Window to open it.
    def __init__(self, master):
        self.open(Home_Window)

    #This function opens the sended window.    
    def open(self, Twindow):
        Twindow(self)

    #This function opens the sended window and check if it's a new game or a saved game.    
    def switch_frame(self, Twindow, saved):
        print(saved)
        Twindow(self, saved)
        
        
#2###########################################################################################################
#Home_Window class: It haves and runs the information of the Home Window        
class Home_Window:

    #This function haves the information of the Home Window.
    def __init__(self, inself):
        global namep

        #Main Window
        self.canvas = Canvas(width = 800, height = 700,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #Title "Clash Rooks"
        self.clash = Label(self.canvas, text= "CLASH", font=("padauk book",46),fg="white",bg="black")
        self.clash.place(x=315,y=50,width=197,height=47)

        self.rooks = Label(self.canvas, text= "ROOKS", font=("padauk book",46),fg="royalblue2",bg="black")
        self.rooks.place(x=310,y=110,width=214,height=47)

        #Label Name
        self.labelname = Label(self.canvas, text = "YOUR NAME:", font=("padauk book",28),fg="white",bg="black")
        self.labelname.place(x=180,y=200,width=240, height=50)

        self.write_name = Entry(self.canvas,font=("padauk book",28),fg="white",bg="black")
        self.write_name.place(x=430, y=205, width=250, height=40)
        
        #Buttons
        self.play = Button(self.canvas, text = "NEW GAME", font=("padauk book",28),fg="white",bg="black",borderwidth=0, command =lambda: [self.playername(),self.del_win(), inself.switch_frame(Game_Win, "new")])
        self.play.place(x=300,y=300,width=240,height=50)

        self.load = Button(self.canvas, text = "LOAD GAME", font=("padauk book",28),fg="white",bg="black",borderwidth=0, command = lambda: [self.del_win(), inself.switch_frame(Game_Win, "load")])
        self.load.place(x=295,y=360,width=250,height=50)

        self.instructions = Button(self.canvas, text = "INSTRUCTIONS", font=("padauk book",28),fg="white",bg="black",borderwidth=0, command = self.instructions)
        self.instructions.place(x=275,y=430,width=290,height=50)

        self.highscores = Button(self.canvas, text = "HIGHSCORES", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.highscores.place(x=280,y=490,width=260,height=50)

        self.credits = Button(self.canvas, text = "CREDITS", font=("padauk book",28),fg="white",bg="black",borderwidth=0,command= self.credits)
        self.credits.place(x=325,y=550,width=180,height=50)

        

    #This fuction gets and saves the name.
    def playername(self):
        global namep
        namep = self.write_name.get()
        
    #Buttons Pressed
    #This fuctions works when the buttons are pressed(opens the other windows).
    def game(self):
        Game_Win(inself)
        
    def instructions(self):
        Instructions_Win()
        
    def credits(self):
        Credits_Win()
        
    def del_win(self):
        self.canvas.destroy()


#3###########################################################################################################
#Game_Window class: It haves and runs the information of the Game_Window.
        
class Game_Win:
    def __init__(self, inself, saved):
        global namep

        #Backgroung
        self.can = Canvas( width = 800, height = 675, highlightthickness = 0, relief='ridge', bg= "black")
        self.can.place(x=0,y=0)

        #Name label
        self.name = Label(self.can, text=namep, font=("padauk book",28),fg="royalblue2",bg="black")
        self.name.place(x=20,y=420,width=150,height=30)

        #Creates the time function to count time
        self.time = 0
        self.timelab = Label(self.can, text= "TIME:" + str(self.time), font=("padauk book",20),fg="white",bg="black")
        self.timelab.place(x=20,y=470,width=140,height=30)
        
        
        
        #Coins Title
        #Creates the coins fuction to count the coins that the player have
        self.coins = 0
        self.coinslab = Label(self.can, text= "COINS:" + str(self.coins), font=("padauk book",20),fg="white",bg="black")
        self.coinslab.place(x=40,y=520,width=140,height=30)

        #Save game Button
        self.save = Button(self.can, text = "Save Game", font=("padauk book",20),fg="white",bg="black",borderwidth=0,command= self.load)
        self.save.place(x=20, y=600)


        

        #Playing the sound
        winsound.PlaySound(os.path.join('Music8bit.wav'), winsound.SND_LOOP|winsound.SND_ASYNC)
        
        #Positions of the matrix/table
        positions = (((300,0, 375,75),(375,0, 450,75),(450,0, 525,75),(525,0, 600,75),(600,0, 675,75)),
                     ((300,75, 375,150),(375,75, 450,150),(450,75, 525,150),(525,75, 600,150),(600,75, 675,150)),
                     ((300,150, 375,225),(375,150, 450,225),(450,150, 525,225),(525,150, 600,225),(600,150, 675,225)),
                     ((300,225, 375,300),(375,225, 450,300),(450,225, 525,300),(525,225, 600,300),(600,225, 675,300)),
                     ((300,300, 375,375),(375,300, 450,375),(450,300, 525,375),(525,300, 600,375),(600,300, 675,375)),
                     ((300,375, 375,450),(375,375, 450,450),(450,375, 525,450),(525,375, 600,450),(600,375, 675,450)),
                     ((300,450, 375,525),(375,450, 450,525),(450,450, 525,525),(525,450, 600,525),(600,450, 675,525)),
                     ((300,525, 375,600),(375,525, 450,600),(450,525, 525,600),(525,525, 600,600),(600,525, 675,600)),
                     ((300,600, 375,675),(375,600, 450,675),(450,600, 525,675),(525,600, 600,675),(600,600, 675,675)))

        
        

        self.table(positions, len(positions), len(positions[0])-1, 0, "C0L0", 0,0, saved)

    #This function counts the seconds
    def timer(self):
        if self.win2 == True:
            self.time += 1
            self.timelab.config(text="TIME:" +str(self.time))
            window.after(1000,self.timer)

    #This function counts the coins and puts new coins randomly in the table        
    def coinscount(self):
        if self.win2 == True:
        
            #Loading coins images
            self.coppercoin = PhotoImage(file = "images\CopperCoin.png")
            self.goldcoin = PhotoImage(file = "images\GoldCoin.png")
            self.silvercoin = PhotoImage(file = "images\SilverCoin.png")
            
            #Where to put the coins
            self.squads2 = (((300,150, 375,225),(375,150, 450,225),(450,150, 525,225),(525,150, 600,225),(600,150, 675,225)),
                         ((300,225, 375,300),(375,225, 450,300),(450,225, 525,300),(525,225, 600,300),(600,225, 675,300)),
                         ((300,300, 375,375),(375,300, 450,375),(450,300, 525,375),(525,300, 600,375),(600,300, 675,375)),
                         ((300,375, 375,450),(375,375, 450,450),(450,375, 525,450),(525,375, 600,450),(600,375, 675,450)),
                         ((300,450, 375,525),(375,450, 450,525),(450,450, 525,525),(525,450, 600,525),(600,450, 675,525)),
                         ((300,525, 375,600),(375,525, 450,600),(450,525, 525,600),(525,525, 600,600),(600,525, 675,600)),
                         ((300,600, 375,675),(375,600, 450,675),(450,600, 525,675),(525,600, 600,675),(600,600, 675,675)))
            
            self.num = random.randint(1,10)

            
            #Copper Coin Appears
            if self.num == 1 or self.num == 2 or self.num == 3 or self.num == 4 or self.num==5:
                self.xcord = random.choice((340,415,490,565,640))
                self.ycord = random.choice((160,235,310,385,460,535,610))
                self.coin = self.can.create_image(self.xcord,self.ycord, anchor=N, image=self.coppercoin, tags= "coin")
                self.can.tag_bind(self.coin, "<Button-1>", lambda event: self.press_coppercoin(event,self.coin))

                
            #Silver Coin Appears
            if self.num == 6 or self.num == 7 or self.num == 8:
                self.xcord = random.choice((340,415,490,565,640))
                self.ycord = random.choice((150,225,300,375,450,525,600))
                self.coin = self.can.create_image(self.xcord,self.ycord, anchor=N, image=self.silvercoin, tags= "coin")
                self.can.tag_bind(self.coin, "<Button-1>", lambda event: self.press_silvercoin(event,self.coin))

            #Gold Coin Appears
            if self.num == 9 or self.num == 10:
                self.xcord = random.choice((340,415,490,565,640))
                self.ycord = random.choice((150,225,300,375,450,525,600))
                self.coin = self.can.create_image(self.xcord,self.ycord, anchor=N, image=self.goldcoin, tags= "coin")
                self.can.tag_bind(self.coin, "<Button-1>", lambda event: self.press_goldcoin(event,self.coin))

    #This functions sums the value of the coin when it's touched.
    def press_coppercoin(self,event,coin):
        self.coins += 25
        self.coinslab.config(text="COINS:" + str(self.coins))
        self.can.delete(coin)
        window.after(7000,self.coinscount)
    def press_silvercoin(self,event,coin):
        self.coins += 50
        self.coinslab.config(text="COINS:" + str(self.coins))
        self.can.delete(coin)
        window.after(7000,self.coinscount)
    def press_goldcoin(self,event,coin):
        self.coins += 100
        self.coinslab.config(text="COINS:" + str(self.coins))
        self.can.delete(coin)
        window.after(7000,self.coinscount)

    #This functions creates the table and the rooks. This also move the firts created rooks.   
    def table(self, positions, columm, lines, color, name, contli, contco, saved):
        global namep
        if contco==columm:
            #In case is was a saved game
            if saved == "load":
                pickle_file=open('data.pickle', 'rb')
                rooks =pickle.load(pickle_file) 
                self.load_game(rooks[0], 0, 1, 2)
                self.time=rooks[1][0]
                self.coin=rooks[1][1]
                namep =rooks[1][2]
                self.name = Label(self.can, text=namep, font=("padauk book",28),fg="royalblue2",bg="black")
                self.name.place(x=20,y=420,width=150,height=30)
                
                
            #Calls the coinscount and time function
            self.win2 = True
            self.coinscount()
            self.timer()

            #A list of the squares names/tags
            self.squads = ["C0L0", "C0L1", "C0L2", "C0L3", "C0L4", "C1L0", "C1L1", "C1L2", "C1L3", "C1L4",
                  "C2L0", "C2L1", "C2L2", "C2L3", "C2L4", "C3L0", "C3L1", "C3L2", "C3L3", "C3L4",
                  "C4L0", "C4L1", "C4L2", "C4L3", "C4L4", "C5L0", "C5L1", "C5L2", "C5L3", "C5L4",
                  "C6L0", "C6L1", "C6L2", "C6L3", "C6L4", "C7L0", "C7L1", "C7L2", "C7L3", "C7L4",
                  "C8L0", "C8L1", "C8L2", "C8L3", "C8L4", "C9L0", "C9L1", "C9L2", "C9L3", "C9L4"]

            #Loading rooks images and getting their id
            self.srook = (PhotoImage(file= os.path.join('images', "sandR.png"))).subsample(2,2)
            self.imageS = self.can.create_image(50, 100, image= self.srook, tags='rook')
            self.can.addtag_withtag("sand", self.imageS)
            self.rrook = (PhotoImage(file= os.path.join('images', "rockR.png"))).subsample(2,2)
            self.imageR = self.can.create_image(50, 180, image= self.rrook, tags='rook')
            self.can.addtag_withtag("rock", self.imageR)
            self.frook = (PhotoImage(file= os.path.join('images', "fireR.png"))).subsample(2,2)
            self.imageR = self.can.create_image(50, 260, image= self.frook, tags='rook')
            self.can.addtag_withtag("fire", self.imageR)
            self.wrook = (PhotoImage(file= os.path.join('images', "waterR.png"))).subsample(2,2)
            self.imageR = self.can.create_image(50, 340, image= self.wrook, tags='rook')
            self.can.addtag_withtag("water", self.imageR)
            self.identi0= self.can.find_overlapping(50, 100, 100, 150)
            self.identi1= self.can.find_overlapping(50, 180, 100, 220)
            self.identi2= self.can.find_overlapping(50, 260, 100, 310)
            self.identi3= self.can.find_overlapping(50, 340, 100, 390)

            

            
    
            
            #Actions when a rook is moved
            ##Sand Rook
            self.can.tag_bind(self.identi0[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi0[0]))   
            self.can.tag_bind(self.identi0[0], "<Button1-Motion>", lambda event: self.move(event,"one"))
            self.can.tag_bind(self.identi0[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"one"))
            self.coinslab.config(text="COINS:" + str(self.coins))
                             
            #Rock rook
            self.can.tag_bind(self.identi1[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi1[0]))
            self.can.tag_bind(self.identi1[0], "<Button1-Motion>", lambda event: self.move(event,"two"))
            self.can.tag_bind(self.identi1[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"two"))
            self.coinslab.config(text="COINS:" + str(self.coins))
                
            #Fire Rook
            self.can.tag_bind(self.identi2[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi2[0]))
            self.can.tag_bind(self.identi2[0], "<Button1-Motion>", lambda event: self.move(event,"three"))
            self.can.tag_bind(self.identi2[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"three"))
            self.coinslab.config(text="COINS:" + str(self.coins))
                
            #Water Rook
            self.can.tag_bind(self.identi3[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi3[0]))
            self.can.tag_bind(self.identi3[0], "<Button1-Motion>", lambda event: self.move(event,"four"))
            self.can.tag_bind(self.identi3[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"four"))
            self.coinslab.config(text="COINS:" + str(self.coins))
            

            #Call the create_avatar function
            self.create_avatar()


        #In case  the box has an uneven position    
        elif contli<=lines and color==0 and contco<=columm:
            self.can.create_rectangle(positions[contco][contli][0], positions[contco][contli][1],
                                         positions[contco][contli][2], positions[contco][contli][3],
                                         width=1, fill='green',tags=name)
            self.can.addtag_withtag("green", name)
            return self.table(positions, columm, lines, 1, name[:-1] + str(int(name[3])+ 1), contli+1, contco, saved)

        #In case  the box has an pair position
        elif contli<=lines and color==1 and contco<=columm:
            self.can.create_rectangle(positions[contco][contli][0], positions[contco][contli][1],
                                         positions[contco][contli][2], positions[contco][contli][3],
                                         width=1, fill='blue',tags=name)
            self.can.addtag_withtag("blue", name)
            return self.table(positions, columm, lines, 0, name[:-1] + str(int(name[3])+ 1), contli+1, contco, saved)

        #In case there is no more lines
        elif contco<columm:
            return self.table(positions, columm, 4, color, "C"+str(int(name[1])+1)+"L0", 0, contco+1, saved)


    #This function calls the other function to create the avatars
    def create_avatar(self):
           
        window.after(3000, lambda :self.arch_avatar())
        window.after(16000, lambda :self.kng_avatar())
        window.after(28000, lambda :self.cann_avatar())
        window.after(45000, lambda :self.lumb_avatar())
        

    def win_time(self):
        self.youwin = Label(self.can, text= "YOU WIN!", font=("padauk book",30),fg="white",bg="black")
        self.youwin.place(x=350,y=360,width=230,height=70)

        self.yourscore = Label(self.can, text= "YOUR SCORE:" + str(5000-self.time), font=("padauk book",20),fg="white",bg="black")
        self.yourscore.place(x=350,y=460,width=280,height=40)

        #Back Button
        self.backbutton = Button(self.can, text = "BACK", font=("padauk book",18),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbutton.place(x=350,y=560,width=90,height=30)

    def backbutton(self):
        self.canvas.destroy()
        
            

    #This functions selects a random place in the last line to put the avatar and calls the move fuction
    def kng_avatar(self):
        rpocition= random.randint(0,4)
        place=self.squads2[6][rpocition]
        x=place[2]-33
        y=place[3]-35
        self.life_knig = 10
        self.move_ava("knig", y, x)
        
    def arch_avatar(self):
        rpocition= random.randint(0,4)
        place=self.squads2[6][rpocition]
        x=place[2]-33
        y=place[3]-35
        self.life_arch = 5
        self.move_ava("arch", y, x)

    def cann_avatar(self):
        rpocition= random.randint(0,4)
        place=self.squads2[6][rpocition]
        x=place[2]-33
        y=place[3]-35
        self.life_cann = 25
        self.move_ava("cann", y, x)

    def lumb_avatar(self):
        rpocition= random.randint(0,4)
        place=self.squads2[6][rpocition]
        x=place[2]-40
        y=place[3]-35
        self.life_lumb = 20
        self.move_ava("lumb", y, x)
        

    #This fuctions creates the images of the avartars and calls the walk fuction
    def move_ava(self, avatar, y, x):
        #In case a avatar reach the upper limit
        if y<=0:
            self.win2=False
            self.youwin = Label(self.can, text= "YOU LOSE :(", font=("padauk book",30),fg="white",bg="black")
            self.youwin.place(x=350,y=360,width=230,height=70)

            self.yourscore = Label(self.can, text= "YOUR SCORE:" + str((5000-self.time)-2500), font=("padauk book",20),fg="white",bg="black")
            self.yourscore.place(x=350,y=460,width=280,height=40)

        #Archer
        if avatar=="arch":
            x_a, y_a = x, y
            self.archer = (PhotoImage(file= os.path.join('images/Archer', "Walk1.png")))
            self.avaimageA = self.can.create_image(x_a, y_a, image= self.archer, tags="arch")
            self.can.addtag_withtag("alive", self.avaimageA)

            if self.life_arch <= 0:
                self.coins+=75
                self.coinslab.config(text="COINS:" + str(self.coins))
                self.can.delete(self.avaimageA)
                self.dead = (PhotoImage(file = os.path.join('images/Archer',"ArcherDead.png")))
                self.deadimage = self.can.create_image(x_a, y_a, image = self.dead)
                window.after(1000,lambda: [self.can.delete(self.deadimage)])
                
            else:
                window.after(1000, lambda: [self.walk("arch", y_a, x_a)])

        #Knight/Shield Bearer        
        elif avatar=="knig":
            x_k, y_k = x, y
            self.knight = (PhotoImage(file= os.path.join('images/Knight', "Walk1.png")))
            self.avaimageK = self.can.create_image(x_k, y_k, image= self.knight, tags="knig")
            self.can.addtag_withtag("alive", self.avaimageK)
            
            if self.life_knig <= 0:
                self.coins+=75
                self.coinslab.config(text="COINS:" + str(self.coins))
                self.can.delete(self.avaimageK)
                self.dead = (PhotoImage(file = os.path.join('images/Knight',"KnightDead.png")))
                self.deadimage = self.can.create_image(x_k, y_k, image = self.dead)
                window.after(1000,lambda: [self.can.delete(self.deadimage)])
                
            else:
                window.after(1000, lambda: [self.walk("knig", y_k, x_k)])

        #Cannibal        
        elif avatar=="cann":
            x_c, y_c = x, y
            self.cannibal = (PhotoImage(file= os.path.join('images/Cannibal', "Walk1.png")))
            self.avaimageC = self.can.create_image(x_c, y_c, image= self.cannibal, tags="cann")
            self.can.addtag_withtag("alive", self.avaimageC)
    
            if self.life_cann <= 0:
                self.coins+=75
                self.coinslab.config(text="COINS:" + str(self.coins))
                self.can.delete(self.avaimageC)
                self.dead = (PhotoImage(file = os.path.join('images/Cannibal',"CannibalDead.png")))
                self.deadimage = self.can.create_image(x_c, y_c, image = self.dead)
                window.after(1000,lambda: [self.can.delete(self.deadimage)])
                
            else:
                window.after(1000, lambda: [self.walk("cann", y_c, x_c)])

        #Lumberjack
        elif avatar=="lumb":
            x_l, y_l = x, y
            self.lumberjack = (PhotoImage(file= os.path.join('images/Lumberjack', "Walk1.png")))
            self.avaimageL = self.can.create_image(x_l, y_l, image= self.lumberjack, tags="lumb")
            self.can.addtag_withtag("alive", self.avaimageL)
            
            if self.life_lumb <= 0:
                self.coins+=75
                self.coinslab.config(text="COINS:" + str(self.coins))
                self.can.delete(self.avaimageL)
                self.dead = (PhotoImage(file = os.path.join('images/Lumberjack',"LumberDead.png")))
                self.deadimage = self.can.create_image(x_l, y_l, image = self.dead)
                window.after(1000,lambda: [self.can.delete(self.deadimage)])
                window.after(4000,lambda: [self.win_time()])
                
            else:
                window.after(1000, lambda: [self.walk("lumb", y_l, x_l)])

        
    #This and the next fuctions moves the avatar (lively) according to time.        
    def walk(self, avatar, y, x):

        #Archer
        if avatar=="arch":
            window.after(12000, lambda: [self.can.delete(self.avaimageA), self.walk1('images/Archer', "Walk2.png", y-30, x)])
            window.after(12000, lambda: [self.can.delete(self.avaimageA), self.walk1('images/Archer', "Walk3.png", y-60, x)])
            window.after(12000, lambda: [self.can.delete(self.avaimageA), self.move_ava(avatar, y-75, x)])

        #Knight 
        elif avatar=="knig":
            window.after(10000, lambda: [self.can.delete(self.avaimageK), self.walk1('images/Knight', "Walk2.png", y-30, x)])
            window.after(10000, lambda: [self.can.delete(self.avaimageK), self.walk1('images/Knight', "Walk3.png", y-60, x)])
            window.after(10000, lambda: [self.can.delete(self.avaimageK), self.move_ava(avatar, y-75, x)])

        #Cannibal
        elif avatar=="cann":
            window.after(14000, lambda: [self.can.delete(self.avaimageC), self.walk1('images/Cannibal', "Walk2.png", y-30, x)])
            window.after(14000, lambda: [self.can.delete(self.avaimageC), self.walk1('images/Cannibal', "Walk3.png", y-60, x)])
            window.after(14000, lambda: [self.can.delete(self.avaimageC), self.move_ava(avatar, y-75, x)])

        #Lumberjack
        elif avatar=="lumb":
            window.after(13000, lambda: [self.can.delete(self.avaimageL), self.walk1('images/Lumberjack', "Walk2.png", y-30, x)])
            window.after(13000, lambda: [self.can.delete(self.avaimageL), self.walk1('images/Lumberjack', "Walk3.png", y-60, x)])
            window.after(13000, lambda: [self.can.delete(self.avaimageL), self.move_ava(avatar, y-75, x)])
                                        

    def walk1(self, location, image, y, x):
        #Archer
        if location[-4:]=="cher":
            self.archer = (PhotoImage(file= os.path.join(location, image)))
            self.avaimageA = self.can.create_image(x, y, image= self.archer, tags="arch")
            self.can.addtag_withtag("alive", self.avaimageA)

        #Knight
        elif location[-4:]=="ight":
            self.knight = (PhotoImage(file= os.path.join(location, image)))
            self.avaimageK = self.can.create_image(x, y, image= self.knight, tags="knig")
            self.can.addtag_withtag("alive", self.avaimageK)

        #Cannibal
        elif location[-4:]=="ibal":
            self.cannibal = (PhotoImage(file= os.path.join(location, image)))
            self.avaimageC = self.can.create_image(x, y, image= self.cannibal, tags="cann")
            self.can.addtag_withtag("alive", self.avaimageC)

        #Lumberjack
        elif location[-4:]=="jack":
            self.lumberjack = (PhotoImage(file= os.path.join(location, image)))
            self.avaimageL = self.can.create_image(x, y, image= self.lumberjack, tags="lumb")
            self.can.addtag_withtag("alive", self.avaimageL)
    
    #This function detect the button pressed    
    def press_boton(self, event, ID):
        rook = ID
        self.selected_rook = (rook, event.x, event.y)

    #This function moves the rooks    
    def move(self,event, tower):
        if (tower == "one" and self.coins>=50) or (tower == "two" and self.coins>=100) or (tower == "three" and self.coins>=150) or (tower == "four" and self.coins>=150):
            x, y = event.x, event.y
            rook, x1, y1 = self.selected_rook
            self.can.move(rook, x-x1, y-y1)
            self.selected_rook = (rook, x, y)
        
    #This function is to load the game
    def load_game(self, rooks, rook, place, color):
        if rook == len(rooks)-3:
            self.create(rooks[rook], rooks[place],(rooks, rook, place,color,  False),rooks[color])
            
        else:
            self.create(rooks[rook], rooks[place],(rooks, rook, place,color, True),rooks[color])
    #This function saves the game        
    def load (self):
        global namep
        pickle_file = open('data.pickle', 'wb')
        
        self.tico = ((self.time, self.coins, namep))
        self.data = (self.data),(self.tico)
        pickle.dump(self.data, pickle_file)
        pickle_file.close()
        pickle_file=open('data.pickle', 'rb')
        data= pickle.load(pickle_file)

    #This functions creates the rooks    
    def create(self, rook, place, info, color):

        #Creating the Sand Tower
        if rook == "one":
            Tower = (PhotoImage(file= os.path.join('images', "sandR.png"))).subsample(2,2)
            dimage = Label(self.can, image=Tower, bg=color)
            dimage.image =  Tower
            dimage.place(x=place[0]+10, y=place[1])

        #Creating the Rock Tower
        elif rook == "two":
            Tower = (PhotoImage(file= os.path.join('images', "rockR.png"))).subsample(2,2)
            dimage = Label(self.can, image=Tower, bg=color)
            dimage.image =  Tower
            dimage.place(x=place[0]+10, y=place[1]-5)

        #Creating the Fire Tower   
        elif rook == "three":
            Tower = (PhotoImage(file= os.path.join('images', "fireR.png"))).subsample(2,2)
            dimage = Label(self.can, image=Tower, bg=color)
            dimage.image =  Tower
            dimage.place(x=place[0]+10, y=place[1])

        #Creating the Water Tower   
        elif rook == "four":
            Tower = (PhotoImage(file= os.path.join('images', "waterR.png"))).subsample(2,2)
            dimage = Label(self.can, image=Tower, bg=color)
            dimage.image =  Tower
            dimage.place(x=place[0]+10, y=place[1])
            
        data = (rook, place, color)
        try:
            self.data= self.data + data
        except:
            self.data= data
        if info ==  "gaming":
            self.rooks(rook)
        else:
            if info[4] == True:
                self.load_game(info[0], info[1]+3, info[2]+3, info[3]+3)

    #this function creat   
    def rooks(self, rook):
        
        if rook == "one":
            self.srook = (PhotoImage(file= os.path.join('images', "sandR.png"))).subsample(2,2)
            self.imageS = self.can.create_image(50, 100, image= self.srook, tags='rook')
            self.can.addtag_withtag("sand", self.imageS)
        elif rook == "two":
            self.rrook = (PhotoImage(file= os.path.join('images', "rockR.png"))).subsample(2,2)
            self.imageR = self.can.create_image(50, 180, image= self.rrook, tags='rook')
            self.can.addtag_withtag("rock", self.imageR)
        elif rook== "three":
            self.frook = (PhotoImage(file= os.path.join('images', "fireR.png"))).subsample(2,2)
            self.imageR = self.can.create_image(50, 260, image= self.frook, tags='rook')
            self.can.addtag_withtag("fire", self.imageR)
        elif rook == "four":
            self.wrook = (PhotoImage(file= os.path.join('images', "waterR.png"))).subsample(2,2)
            self.imageR = self.can.create_image(50, 340, image= self.wrook, tags='rook')
            self.can.addtag_withtag("water", self.imageR)
        self.identi0= self.can.find_overlapping(50, 100, 100, 150)
        self.identi1= self.can.find_overlapping(50, 180, 100, 220)
        self.identi2= self.can.find_overlapping(50, 260, 100, 310)
        self.identi3= self.can.find_overlapping(50, 340, 100, 390)
        

        #This is to move the rooks
        self.can.tag_bind(self.identi0[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi0[0]))  
        self.can.tag_bind(self.identi0[0], "<Button1-Motion>", lambda event: self.move(event,"one"))
        self.can.tag_bind(self.identi0[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"one"))
        
                
        self.can.tag_bind(self.identi1[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi1[0]))
        self.can.tag_bind(self.identi1[0], "<Button1-Motion>", lambda event: self.move(event,"two"))
        self.can.tag_bind(self.identi1[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"two"))
        
                
  
        self.can.tag_bind(self.identi2[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi2[0]))
        self.can.tag_bind(self.identi2[0], "<Button1-Motion>", lambda event: self.move(event,"three"))
        self.can.tag_bind(self.identi2[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"three"))
        
                

        self.can.tag_bind(self.identi3[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi3[0]))
        self.can.tag_bind(self.identi3[0], "<Button1-Motion>", lambda event: self.move(event,"four"))
        self.can.tag_bind(self.identi3[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"four"))
            


    #This function is to create the arrows    
    def shoot(self, rook, position):

        #Sand Tower
        if rook=="one":
            Spoints=(position[0]+30,position[1]+40, position[0]+20,position[1]+60,
                    position[0]+30,position[1]+70, position[0]+40,position[1]+60)
            self.rang=self.can.find_enclosed(position[0]-2, position[1], position[2]-2, position[3]+900)
            
            if len(self.rang)> 0 and (self.can.gettags(self.rang[-1])[-1]=="alive"or self.can.gettags(self.rang[-1])[1]=="coin"):
                self.Sarrow =self.can.create_polygon(Spoints,width=1,outline="black", fill="darkorange3", tags= "Sarrow")
                self.can.addtag_withtag("2", self.Sarrow)
                self.limit=Spoints[5]+100

        #Rock Tower
        if rook=="two":
            Rpoints=(position[0]+30,position[1]+40, position[0]+20,position[1]+60,
                    position[0]+30,position[1]+70, position[0]+40,position[1]+60)
            rang=self.can.find_enclosed(position[0]-2, position[1], position[2]-2, position[3]+800)
            if len(rang)> 0 and (self.can.gettags(self.rang[-1])[-1]=="alive"or self.can.gettags(self.rang[-1])[1]=="coin"):
                self.Rarrow =self.can.create_polygon(Rpoints,width=1,outline="black", fill="gray40", tags= "Rarrow")
                self.can.addtag_withtag("4", self.Rarrow)
                self.limit=Rpoints[5]+100

        #Fire Towe
        if rook=="three":
            Fpoints=(position[0]+30,position[1]+40, position[0]+20,position[1]+60,
                    position[0]+30,position[1]+70, position[0]+40,position[1]+60)
            rang=self.can.find_enclosed(position[0]-2, position[1], position[2]-2, position[3]+800)
            if len(rang)> 0 and (self.can.gettags(self.rang[-1])[-1]=="alive"or self.can.gettags(self.rang[-1])[1]=="coin"):
                self.Farrow =self.can.create_polygon(Fpoints,width=1,outline="black", fill="darkorange1", tags= "Farrow")
                self.can.addtag_withtag("8", self.Farrow)
                self.limit=Fpoints[5]+100

        #Water Tower
        if rook=="four":
            Wpoints=(position[0]+30,position[1]+40, position[0]+20,position[1]+60,
                    position[0]+30,position[1]+70, position[0]+40,position[1]+60)
            rang=self.can.find_enclosed(position[0]-2, position[1], position[2]-2, position[3]+800)
            if len(rang)> 0 and (self.can.gettags(self.rang[-1])[-1]=="alive" or self.can.gettags(self.rang[-1])[1]=="coin"):
                self.Warrow =self.can.create_polygon(Wpoints,width=1,outline="black", fill="dodgerblue3", tags= "Warrow")
                self.can.addtag_withtag("8", self.Warrow)
                self.limit=Wpoints[5]+100
                

                
    #Loops for the motion of the arrows                           
    def arrow_loop1(self ,rook, position):
        self.movement(rook, position)
        self.can.after(300,lambda : [self.arrow_loop1(rook, position)])
            
    def arrow_loop2(self, rook, position):
        self.movement2(rook, position)
        self.can.after(300,lambda : [self.arrow_loop2(rook, position)])
            
    def arrow_loop3(self, rook, position):
        self.movement3(rook, position)
        self.can.after(300,lambda : [self.arrow_loop3(rook, position)])
            
    def arrow_loop4(self, rook, position):
        self.movement4(rook, position)
        self.can.after(300,lambda : [self.arrow_loop4(rook, position)])
        
        
    #This functions are to move the arrows

    #Sand tower    
    def movement(self, rook, position):
        
        try:
            
            self.can.move("Sarrow", 0, +5)
            arrow=self.can.find_withtag("Sarrow")[0]
            posc = self.can.coords(self.Sarrow) 
            crash=self.can.bbox(arrow)
            touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])


            if self.can.gettags(touch[-1])[0]=="arch" or self.can.gettags(touch[-1])[0]=="knig" or self.can.gettags(touch[-1])[0]=="cann" or self.can.gettags(touch[-1])[0]=="lumb":

                if self.can.gettags(touch[-1])[0]=="arch":
                    self.life_arch -= 2
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="knig":
                    self.life_knig -= 2
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="cann":
                    self.life_cann -= 2
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="lumb":
                    self.life_lumb -= 2
                    self.can.delete(arrow)

            if posc[5]>self.limit:
                self.shoot(rook, position)

        except:
            try:
                self.can.move("Sarrow", 0, +5)
            except:
                self.can.after(3000,lambda : [self.arrow_loop1(rook, position)])

    #Rock Tower            
    def movement2(self,rook, position):
        try:
            
            self.can.move("Rarrow", 0, +5)
            arrow=self.can.find_withtag("Rarrow")[0]
            posc = self.can.coords(self.Rarrow)  
            crash=self.can.bbox(arrow)
            touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])


            if self.can.gettags(touch[-1])[0]=="arch" or self.can.gettags(touch[-1])[0]=="knig" or self.can.gettags(touch[-1])[0]=="cann" or self.can.gettags(touch[-1])[0]=="lumb":

                if self.can.gettags(touch[-1])[0]=="arch":
                    self.life_arch -= 4
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="knig":
                    self.life_knig -= 4
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="cann":
                    self.life_cann -= 4
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="lumb":
                    self.life_lumb -= 4
                    self.can.delete(arrow)
            
            

            if posc[5]>self.limit:
                self.shoot(rook, position)

        except:
            try:
                self.can.move("Rarrow", 0, +5)
            except:
                self.can.after(3000,lambda : [self.arrow_loop2(rook, position)])

    #Fire Tower
    def movement3(self,rook, position):
        try:
            self.can.move("Farrow", 0, +5)
            arrow=self.can.find_withtag("Farrow")[0]
            posc = self.can.coords(self.Farrow)   
            crash=self.can.bbox(arrow)
            touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])

            if self.can.gettags(touch[-1])[0]=="arch" or self.can.gettags(touch[-1])[0]=="knig" or self.can.gettags(touch[-1])[0]=="cann" or self.can.gettags(touch[-1])[0]=="lumb":

                if self.can.gettags(touch[-1])[0]=="arch":
                    self.life_arch -= 8
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="knig":
                    self.life_knig -= 8
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="cann":
                    self.life_cann -= 8
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="lumb":
                    self.life_lumb -= 8
                    self.can.delete(arrow)

            if posc[5]>self.limit:
                self.shoot(rook, position)

        except:
            try:
                self.can.move("Farrow", 0, +5)
            except:
                self.can.after(3000,lambda : [self.arrow_loop3(rook, position)])
                

    #Water tower
    def movement4(self,rook, position):
        try:
            self.can.move("Warrow", 0, +5)
            arrow=self.can.find_withtag("Warrow")[0]
            posc = self.can.coords(self.Warrow)   
            crash=self.can.bbox(arrow)
            touch=self.can.find_overlapping(crash[0], crash[1], crash[2], crash[3])

            if self.can.gettags(touch[-1])[0]=="arch" or self.can.gettags(touch[-1])[0]=="knig" or self.can.gettags(touch[-1])[0]=="cann" or self.can.gettags(touch[-1])[0]=="lumb":

                if self.can.gettags(touch[-1])[0]=="arch":
                    self.life_arch -= 8
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="knig":
                    self.life_knig -= 8
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="cann":
                    self.life_cann -= 8
                    self.can.delete(arrow)

                if self.can.gettags(touch[-1])[0]=="lumb":
                    self.life_lumb -= 8
                    self.can.delete(arrow)

            if posc[5]>self.limit:
                self.shoot(rook, position)

        except:
            try:
                self.can.move("Warrow", 0, +5)
            except:
                self.can.after(3000,lambda : [self.arrow_loop4(rook, position)])
    
        


    #This function is when a rook is placed
    def new_position(self, event ,rook):
        
        if (rook == "one" and self.coins>=50) or (rook == "two" and self.coins>=100) or (rook == "three" and self.coins>=150) or (rook == "four" and self.coins>=150):

            #Placing the Sand Tower
            if rook=="one":
                ID=self.identi0[0]
                over=self.can.coords(ID)
                squad_id=self.can.find_overlapping(over[0], over[1], over[0]+20, over[1]+10)[0]
                color=(self.can.gettags(squad_id)[1])
                squad_id=(self.can.gettags(squad_id)[0])
                if self.can.coords(self.squads[0])[0]-10<=over[0]<=self.can.coords(self.squads[0])[2] and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L0'and self.squads[0][-1]!="F":
                    full = self.squads[0]+"F"
                    self.can.addtag_withtag(full, self.squads[0])
                    self.squads[0] = full
                    self.can.delete(ID)
                    lis=(310,10, 365,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                    
                elif self.can.coords(self.squads[1])[0]-10<=over[0]<=self.can.coords(self.squads[1])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L1'and self.squads[1][-1]!="F":
                    full = self.squads[1]+"F"
                    self.can.addtag_withtag(full, self.squads[1])
                    self.squads[1] = full
                    self.can.delete(ID)
                    lis = (385,10, 440,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                    
                elif self.can.coords(self.squads[2])[0]-10<=over[0]<=self.can.coords(self.squads[2])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L2'and self.squads[2][-1]!="F":
                    full = self.squads[2]+"F"
                    self.can.addtag_withtag(full, self.squads[2])
                    self.squads[2] = full
                    self.can.delete(ID)
                    lis=(460,10, 515,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                    
                elif self.can.coords(self.squads[3])[0]-10<=over[0]<=self.can.coords(self.squads[3])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L3'and self.squads[3][-1]!="F":
                    full = self.squads[3]+"F"
                    self.can.addtag_withtag(full, self.squads[3])
                    self.squads[3] = full
                    self.can.delete(ID)
                    lis=(535,10, 590,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                    
                elif self.can.coords(self.squads[4])[0]-10<=over[0]<=self.can.coords(self.squads[4])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L4'and self.squads[4][-1]!="F":
                    full = self.squads[4]+"F"
                    self.can.addtag_withtag(full, self.squads[4])
                    self.squads[4] = full
                    self.can.delete(ID)
                    lis=(610,10, 665,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                    
                elif self.can.coords(self.squads[5])[0]-10<=over[0]<=self.can.coords(self.squads[5])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L0'and self.squads[5][-1]!="F":
                    full = self.squads[5]+"F"
                    self.can.addtag_withtag(full, self.squads[5])
                    self.squads[5] = full
                    self.can.delete(ID)
                    lis=(310,85, 365,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                elif self.can.coords(self.squads[6])[0]-10<=over[0]<=self.can.coords(self.squads[6])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L1'and self.squads[6][-1]!="F":
                    full = self.squads[6]+"F"
                    self.can.addtag_withtag(full, self.squads[6])
                    self.squads[6] = full
                    self.can.delete(ID)
                    lis=(385,85, 440,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                elif self.can.coords(self.squads[7])[0]-10<=over[0]<=self.can.coords(self.squads[7])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L2'and self.squads[7][-1]!="F":
                    full = self.squads[7]+"F"
                    self.can.addtag_withtag(full, self.squads[7])
                    self.squads[7] = full
                    self.can.delete(ID)
                    lis=(460,85, 515,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                elif self.can.coords(self.squads[8])[0]-10<=over[0]<=self.can.coords(self.squads[8])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L3'and self.squads[8][-1]!="F":
                    full = self.squads[8]+"F"
                    self.can.addtag_withtag(full, self.squads[8])
                    self.squads[8] = full
                    self.can.delete(ID)
                    lis=(535,85, 590,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)
                elif self.can.coords(self.squads[9])[0]-10<=over[0]<=self.can.coords(self.squads[9])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L4'and self.squads[9][-1]!="F":
                    full = self.squads[9]+"F"
                    self.can.addtag_withtag(full, self.squads[9])
                    self.squads[9] = full
                    self.can.delete(ID)
                    lis=(610,85, 665,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=50
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop1(rook, lis)

                else:

                    self.can.coords(ID, 50, 100)
                              

                        
            #Placing the Rock Tower        
            elif rook == "two":
                ID=self.identi1[0]
                over=self.can.coords(ID)
                squad_id=self.can.find_overlapping(over[0], over[1], over[0]+20, over[1]+10)[0]
                color=(self.can.gettags(squad_id)[1])
                squad_id=(self.can.gettags(squad_id)[0])
                if self.can.coords(self.squads[0])[0]-10<=over[0]<=self.can.coords(self.squads[0])[2] and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L0'and self.squads[0][-1]!="F":
                    full = self.squads[0]+"F"
                    self.can.addtag_withtag(full, self.squads[0])
                    self.squads[0] = full
                    self.can.delete(ID)
                    lis=(310,10, 365,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[1])[0]-10<=over[0]<=self.can.coords(self.squads[1])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L1'and self.squads[1][-1]!="F":
                    full = self.squads[1]+"F"
                    self.can.addtag_withtag(full, self.squads[1])
                    self.squads[1] = full
                    self.can.delete(ID)
                    lis = (385,10, 440,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[2])[0]-10<=over[0]<=self.can.coords(self.squads[2])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L2'and self.squads[2][-1]!="F":
                    full = self.squads[2]+"F"
                    self.can.addtag_withtag(full, self.squads[2])
                    self.squads[2] = full
                    self.can.delete(ID)
                    lis=(460,10, 515,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[3])[0]-10<=over[0]<=self.can.coords(self.squads[3])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L3'and self.squads[3][-1]!="F":
                    full = self.squads[3]+"F"
                    self.can.addtag_withtag(full, self.squads[3])
                    self.squads[3] = full
                    self.can.delete(ID)
                    lis=(535,10, 590,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[4])[0]-10<=over[0]<=self.can.coords(self.squads[4])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L4'and self.squads[4][-1]!="F":
                    full = self.squads[4]+"F"
                    self.can.addtag_withtag(full, self.squads[4])
                    self.squads[4] = full
                    self.can.delete(ID)
                    lis=(610,10, 665,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[5])[0]-10<=over[0]<=self.can.coords(self.squads[5])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L0'and self.squads[5][-1]!="F":
                    full = self.squads[5]+"F"
                    self.can.addtag_withtag(full, self.squads[5])
                    self.squads[5] = full
                    self.can.delete(ID)
                    lis=(310,85, 365,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[6])[0]-10<=over[0]<=self.can.coords(self.squads[6])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L1'and self.squads[6][-1]!="F":
                    full = self.squads[6]+"F"
                    self.can.addtag_withtag(full, self.squads[6])
                    self.squads[6] = full
                    self.can.delete(ID)
                    lis=(385,85, 440,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[7])[0]-10<=over[0]<=self.can.coords(self.squads[7])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L2'and self.squads[7][-1]!="F":
                    full = self.squads[7]+"F"
                    self.can.addtag_withtag(full, self.squads[7])
                    self.squads[7] = full
                    self.can.delete(ID)
                    lis=(460,85, 515,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[8])[0]-10<=over[0]<=self.can.coords(self.squads[8])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L3'and self.squads[8][-1]!="F":
                    full = self.squads[8]+"F"
                    self.can.addtag_withtag(full, self.squads[8])
                    self.squads[8] = full
                    self.can.delete(ID)
                    lis=(535,85, 590,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)
                    
                elif self.can.coords(self.squads[9])[0]-10<=over[0]<=self.can.coords(self.squads[9])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L4'and self.squads[9][-1]!="F":
                    full = self.squads[9]+"F"
                    self.can.addtag_withtag(full, self.squads[9])
                    self.squads[9] = full
                    self.can.delete(ID)
                    lis=(610,85, 665,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=100
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop2(rook, lis)

                else:
                    
                    self.can.coords(ID, 50, 180)
                            
                   
                
            #Placing the Fire Tower    
            elif rook=="three":
                ID=self.identi2[0]
                over=self.can.coords(ID)
                squad_id=self.can.find_overlapping(over[0], over[1], over[0]+20, over[1]+10)[0]
                color=(self.can.gettags(squad_id)[1])
                squad_id=(self.can.gettags(squad_id)[0])
                if self.can.coords(self.squads[0])[0]-10<=over[0]<=self.can.coords(self.squads[0])[2] and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L0'and self.squads[0][-1]!="F":
                    full = self.squads[0]+"F"
                    self.can.addtag_withtag(full, self.squads[0])
                    self.squads[0] = full
                    self.can.delete(ID)
                    lis=(310,10, 365,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                           
                elif self.can.coords(self.squads[1])[0]-10<=over[0]<=self.can.coords(self.squads[1])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L1'and self.squads[1][-1]!="F":
                    full = self.squads[1]+"F"
                    self.can.addtag_withtag(full, self.squads[1])
                    self.squads[1] = full
                    self.can.delete(ID)
                    lis = (385,10, 440,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[2])[0]-10<=over[0]<=self.can.coords(self.squads[2])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L2'and self.squads[2][-1]!="F":
                    full = self.squads[2]+"F"
                    self.can.addtag_withtag(full, self.squads[2])
                    self.squads[2] = full
                    self.can.delete(ID)
                    lis=(460,10, 515,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                elif self.can.coords(self.squads[3])[0]-10<=over[0]<=self.can.coords(self.squads[3])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L3'and self.squads[3][-1]!="F":
                    full = self.squads[3]+"F"
                    self.can.addtag_withtag(full, self.squads[3])
                    self.squads[3] = full
                    self.can.delete(ID)
                    lis=(535,10, 590,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[4])[0]-10<=over[0]<=self.can.coords(self.squads[4])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L4'and self.squads[4][-1]!="F":
                    full = self.squads[4]+"F"
                    self.can.addtag_withtag(full, self.squads[4])
                    self.squads[4] = full
                    self.can.delete(ID)
                    lis=(610,10, 665,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[5])[0]-10<=over[0]<=self.can.coords(self.squads[5])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L0'and self.squads[5][-1]!="F":
                    full = self.squads[5]+"F"
                    self.can.addtag_withtag(full, self.squads[5])
                    self.squads[5] = full
                    self.can.delete(ID)
                    lis=(310,85, 365,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[6])[0]-10<=over[0]<=self.can.coords(self.squads[6])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L1'and self.squads[6][-1]!="F":
                    full = self.squads[6]+"F"
                    self.can.addtag_withtag(full, self.squads[6])
                    self.squads[6] = full
                    self.can.delete(ID)
                    lis=(385,85, 440,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[7])[0]-10<=over[0]<=self.can.coords(self.squads[7])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L2'and self.squads[7][-1]!="F":
                    full = self.squads[7]+"F"
                    self.can.addtag_withtag(full, self.squads[7])
                    self.squads[7] = full
                    self.can.delete(ID)
                    lis=(460,85, 515,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[8])[0]-10<=over[0]<=self.can.coords(self.squads[8])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L3'and self.squads[8][-1]!="F":
                    full = self.squads[8]+"F"
                    self.can.addtag_withtag(full, self.squads[8])
                    self.squads[8] = full
                    self.can.delete(ID)
                    lis=(535,85, 590,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)
                    
                elif self.can.coords(self.squads[9])[0]-10<=over[0]<=self.can.coords(self.squads[9])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L4'and self.squads[9][-1]!="F":
                    full = self.squads[9]+"F"
                    self.can.addtag_withtag(full, self.squads[9])
                    self.squads[9] = full
                    self.can.delete(ID)
                    lis=(610,85, 665,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop3(rook, lis)

                else:
                    
                    self.can.coords(ID, 50, 260)
                            
                    
            #Placing the Water Tower            
            elif rook=="four":
                ID=self.identi3[0]
                over=self.can.coords(ID)
                squad_id=self.can.find_overlapping(over[0], over[1], over[0]+20, over[1]+10)[0]
                color=(self.can.gettags(squad_id)[1])
                squad_id=(self.can.gettags(squad_id)[0])
                if self.can.coords(self.squads[0])[0]-10<=over[0]<=self.can.coords(self.squads[0])[2] and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L0'and self.squads[0][-1]!="F":
                    full = self.squads[0]+"F"
                    self.can.addtag_withtag(full, self.squads[0])
                    self.squads[0] = full
                    self.can.delete(ID)
                    lis=(310,10, 365,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                elif self.can.coords(self.squads[1])[0]-10<=over[0]<=self.can.coords(self.squads[1])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L1'and self.squads[1][-1]!="F":
                    full = self.squads[1]+"F"
                    self.can.addtag_withtag(full, self.squads[1])
                    self.squads[1] = full
                    self.can.delete(ID)
                    lis = (385,10, 440,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[2])[0]-10<=over[0]<=self.can.coords(self.squads[2])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L2'and self.squads[2][-1]!="F":
                    full = self.squads[2]+"F"
                    self.can.addtag_withtag(full, self.squads[2])
                    self.squads[2] = full
                    self.can.delete(ID)
                    lis=(460,10, 515,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[3])[0]-10<=over[0]<=self.can.coords(self.squads[3])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L3'and self.squads[3][-1]!="F":
                    full = self.squads[3]+"F"
                    self.can.addtag_withtag(full, self.squads[3])
                    self.squads[3] = full
                    self.can.delete(ID)
                    lis=(535,10, 590,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[4])[0]-10<=over[0]<=self.can.coords(self.squads[4])[2]and self.can.coords(self.squads[0])[1]<=over[1]<=self.can.coords(self.squads[0])[3]and squad_id=='C0L4'and self.squads[4][-1]!="F":
                    full = self.squads[4]+"F"
                    self.can.addtag_withtag(full, self.squads[4])
                    self.squads[4] = full
                    self.can.delete(ID)
                    lis=(610,10, 665,65)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[5])[0]-10<=over[0]<=self.can.coords(self.squads[5])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L0'and self.squads[5][-1]!="F":
                    full = self.squads[5]+"F"
                    self.can.addtag_withtag(full, self.squads[5])
                    self.squads[5] = full
                    self.can.delete(ID)
                    lis=(310,85, 365,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[6])[0]-10<=over[0]<=self.can.coords(self.squads[6])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L1'and self.squads[6][-1]!="F":
                    full = self.squads[6]+"F"
                    self.can.addtag_withtag(full, self.squads[6])
                    self.squads[6] = full
                    self.can.delete(ID)
                    lis=(385,85, 440,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[7])[0]-10<=over[0]<=self.can.coords(self.squads[7])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L2'and self.squads[7][-1]!="F":
                    full = self.squads[7]+"F"
                    self.can.addtag_withtag(full, self.squads[7])
                    self.squads[7] = full
                    self.can.delete(ID)
                    lis=(460,85, 515,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[8])[0]-10<=over[0]<=self.can.coords(self.squads[8])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L3'and self.squads[8][-1]!="F":
                    full = self.squads[8]+"F"
                    self.can.addtag_withtag(full, self.squads[8])
                    self.squads[8] = full
                    self.can.delete(ID)
                    lis=(535,85, 590,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)
                    
                elif self.can.coords(self.squads[9])[0]-10<=over[0]<=self.can.coords(self.squads[9])[2]and self.can.coords(self.squads[5])[1]<=over[1]<=self.can.coords(self.squads[5])[3]and squad_id=='C1L4'and self.squads[9][-1]!="F":
                    full = self.squads[9]+"F"
                    self.can.addtag_withtag(full, self.squads[9])
                    self.squads[9] = full
                    self.can.delete(ID)
                    lis=(610,85, 665,140)
                    self.create(rook, lis, "gaming", color)
                    self.coins-=150
                    self.coinslab.config(text="COINS:" + str(self.coins))
                    self.shoot(rook, lis)
                    self.arrow_loop4(rook, lis)

                else:
                    
                    self.can.coords(ID, 50, 340)
                    
            

#4###########################################################################################################
#Instructions_Window class: It haves the instructions to understand the game.          

class Instructions_Win:
    
    def __init__(self):
        
        self.canvas = Canvas(window, width = 800, height = 600,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #All the instructions
        title = "INSTRUCTIONS"
        self.inst2 = Label(self.canvas, text = title, font=("padauk book",30),fg="royalblue2",bg="black",borderwidth=0)
        self.inst2.place(x=250,y=20,width=300,height=30)
        
        instructions = '''You have to stop the avatars using your rooks!\n You have some different types of rooks like:\n\n
        Sand Rook: This rook costs 50 coins and has 2 points of \ndamage and resists 10 point of damage.\n Rock Rook: This rook costs 100 coins and has 4 points of
        damage and resists 14 point of damage.\nFire Rook: This rook costs 150 coins and has 8 points of \ndamage and resists 16 point of damage
        Water Rook: This rook costs 150 coins and has 8 points of \ndamage and resists 16 point of damage.\n\n If you have enough coins,you put this
    towers to defend your kingdom'''
        self.inst = Label(self.canvas, text = instructions, font=("padauk book",20),fg="white",bg="black",borderwidth=0)
        self.inst.place(x=10,y=60,width=750,height=500)

        #Back Button
        self.backbutton = Button(self.canvas, text = "BACK", font=("padauk book",30),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbutton.place(x=340,y=560,width=130,height=40)

    def backbutton(self):
        self.canvas.destroy()
        
             

        
#5###########################################################################################################
#Credits_Window class: It haves all the credits from the game.
class Credits_Win:

    def __init__(self):

        self.canvas = Canvas(window, width = 800, height = 600,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #All the credits
        self.country = Label(self.canvas,text = "COSTA RICA", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.country.place(x=10,y=10,width=244,height=30)       

        self.university = Label(self.canvas,text = "ITCR", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.university.place(x=10,y=50,width=100,height=30)
        
        self.career = Label(self.canvas,text = "COMPUTER ENGINEERING", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.career.place(x=10,y=90,width=520,height=30)

        self.professor = Label(self.canvas,text = "PROF. LUIS BARBOZA ARTAVIA", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.professor.place(x=10,y=130,width=610,height=30)

        self.version = Label(self.canvas,text = "CLASH ROOKS V1", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.version.place(x=10,y=170,width=350,height=30)

        self.author = Label(self.canvas,text = "GONZALO ACUÑA MADRIGAL", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.author.place(x=10,y=210,width=570,height=30)

        self.author1 = Label(self.canvas,text = "FRANCISCO ZAMORA CORRALES", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.author1.place(x=10,y=250,width=650,height=30)

        self.year = Label(self.canvas,text = "2020", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.year.place(x=10,y=290,width=90,height=30)

        self.credits = Label(self.canvas,text = "-------------------------CREDITS-------------------------", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.credits.place(x=0,y=370,width=800,height=30)

        #Back Button
        self.backbutton = Button(self.canvas, text = "BACK", font=("padauk book",30),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbutton.place(x=340,y=450,width=120,height=50)

    def backbutton(self):
        self.canvas.destroy()



if __name__ == "__main__":
    window = Tk()
    home_window = Open_Window(window)
    window.title("Clash Rooks")
    window.minsize(800,700)
