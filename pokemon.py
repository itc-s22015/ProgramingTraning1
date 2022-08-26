from logging import root
import sys
import random
import tkinter as tk
from PIL import Image, ImageTk
import time

class ponnkemon:
    def __init__(self,tkkk):
        self.root = tkkk
        #self.root.title(u"pokemon")
        #self.root.geometry("345x230")
        #root.mainloop()
        self.damage = random.randint(3,5)

        self.image = Image.open("bbb.png")
        self.bg_img = ImageTk.PhotoImage(self.image, master=self.root)
        self.bg = tk.Label(self.root, image=self.bg_img)
        self.bg.place(x=1,y=1)

        self.img_teki = Image.open("osasimi.png")
        self.zeni_img = ImageTk.PhotoImage(self.img_teki,master=self.root)
        self.zeni = tk.Label(self.root, image=self.zeni_img)
        self.zeni.place(x=320,y=40)

        self.bar = tk.Label(background="#555555")
        self.hp = 0.2
        self.bar.place(x=100, y=81.5, relheight=0.02, relwidth=self.hp)
        self.damage = 0
        self.message = tk.Label(text=u"ひっかく"+ str(self.damage)+ "のダメージ")
        
        self.osasimi = tk.Label(text=u"コイキング")
        self.osasimi.place(x=50,y=51)
        
        btn_x = 172
        btn_y = btn_x -14

        self.Button1 = tk.Button(text=u"たたかう",width=6,command=self.attack) 
        self.Button1.place(x=320,y=295)     
        self.Button2 = tk.Button(text=u"どうぐ",width=6,command=self.use_item) 
        self.Button2.place(x=320,y=295+35) 
        self.Button3 = tk.Button(text=u"ポケモン",width=6,command=self.pokemon) 
        self.Button3.place(x=330+70,y=295) 
        self.Button4 = tk.Button(text=u"にげる",width=6,command=self.nigeru) 
        self.Button4.place(x=330+70,y=295+35) 
        
        
        self.root.mainloop()

    def attack(self):
        global hp,damage,message
        self.message.place_forget()
        damage = random.randint(3,5)
        self.hp -= 0.02*damage
        self.bar.place(x=100, y=81.5, relheight=0.02, relwidth=self.hp)
        self.message = tk.Label(text=u"ひっかく"+str(damage)+"のダメージ　　　　　")
        self.message.place(x=70, y=320)
        if self.hp <=0:
            win = tk.Label(text=u"コイキング　を　たおした　　　　　　")
            win.place(x=70,y=320)
            self.zeni.place_forget()

            canvas = tk.Canvas(self.root, width=500, height=400, bd=False, highlightthickness=False)
            canvas.place(x=0,y=0)
            canvas.create_text(250, 180, text="コイキングをたおした", font=("system",30), fill="red")
            canvas.create_text(250, 220, text="GAME CLEAR", font=("system",30), fill="red")
            
            
    def use_item(self):
        dougu = tk.Label(text="どうぐ を もっていない　　　　　　")
        dougu.place(x=70,y=320)

    def pokemon(self):
        poke = tk.Label(text="ほかのポケモン　を　もっていない")
        poke.place(x=70,y=320)
        
    def nigeru(self):
        nige = tk.Label(text="にげられなかった　　　　　　　　")
        nige.place(x=70,y=320)
        
    '''
        btn_x = 172
        btn_y = btn_x -14

        self.Button1 = tk.Button(text=u"たたかう",width=6,command=attack) 
        self.Button1.place(x=btn_x,y=btn_y)       
        self.Button2 = tk.Button(text=u"どうぐ",width=6,command=use_item) 
        self.Button2.place(x=btn_x,y=btn_y+25) 
        self.Button3 = tk.Button(text=u"ポケモン",width=6,command=pokemon) 
        self.Button3.place(x=btn_x+50,y=btn_y) 
        self.Button4 = tk.Button(text=u"にげる",width=6,command=attack) 
        self.Button4.place(x=btn_x+50,y=btn_y+25) 
    '''






        #self.root.mainloop()
#ponnkemon()