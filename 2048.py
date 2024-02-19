import random as r
import time
import customtkinter

root = customtkinter.CTk()
#root.iconbitmap("icon.ico")
labels = [] #spielfeld (als Label)

#trigger bei tastendruck
def handle_key(event):
    i = 0
    while i < 3:
        i = i + 1
        merge(event.keysym)
 #   time.sleep(0.2) #fuers feeling
    newnumber()
    handle_color()

#fügt neue Zahl hinzu
def newnumber():
    empty_labels = [label for label in labels if label.cget("text") == 0]
    if empty_labels:
        random_label = r.choice(empty_labels)
        random_label.configure(text=1)
    else:
        print("VERLOREN!!!!")
        quit()

#"drückt" alle Zahlen in gewünschte Richtung 
#und fügt gleiche Zahlen zusammen
def merge(direction):
    if direction == "Up" or direction == "w" or direction == "W":
        i = 0
        while i <= 11:
            if labels[4+i].cget("text") != 0:
                if labels[0+i].cget("text") == 0:
                    labels[0+i].configure(text=labels[4+i].cget("text"))
                    labels[4+i].configure(text=0)
                elif(labels[0+i].cget("text") == labels[4+i].cget("text")):
                    labels[0+i].configure(text=labels[0+i].cget("text")*2)
                    labels[4+i].configure(text=0)
            i = i + 1
    elif direction == "Down" or direction == "s" or direction == "S":
        i = 11
        while i >= 0:
            if labels[0+i].cget("text") != 0:
                if labels[4+i].cget("text") == 0:
                    labels[4+i].configure(text=labels[0+i].cget("text"))
                    labels[0+i].configure(text=0)
                elif(labels[0+i].cget("text") == labels[4+i].cget("text")):
                    labels[4+i].configure(text=labels[4+i].cget("text")*2)
                    labels[0+i].configure(text=0)
            i = i - 1     
    elif direction == "Left" or direction == "a" or direction == "A":
        i = 0
        while i <= 12:
            if labels[1+i].cget("text") != 0:
                if labels[0+i].cget("text") == 0:
                    labels[0+i].configure(text=labels[1+i].cget("text"))
                    labels[1+i].configure(text=0)
                elif(labels[1+i].cget("text") == labels[0+i].cget("text")):
                    labels[0+i].configure(text=labels[0+i].cget("text")*2)
                    labels[1+i].configure(text=0)
            if labels[2+i].cget("text") != 0:
                if labels[1+i].cget("text") == 0:
                    labels[1+i].configure(text=labels[2+i].cget("text"))
                    labels[2+i].configure(text=0)
                elif(labels[2+i].cget("text") == labels[1+i].cget("text")):
                    labels[1+i].configure(text=labels[1+i].cget("text")*2)
                    labels[2+i].configure(text=0)
            if labels[3+i].cget("text") != 0:
                if labels[2+i].cget("text") == 0:
                    labels[2+i].configure(text=labels[3+i].cget("text"))
                    labels[3+i].configure(text=0)
                elif(labels[3+i].cget("text") == labels[2+i].cget("text")):
                    labels[2+i].configure(text=labels[2+i].cget("text")*2)
                    labels[3+i].configure(text=0)
            i = i + 4
    elif direction == "Right" or direction == "d" or direction == "D":
        i = 0
        while i <= 15:
            if labels[2+i].cget("text") != 0:
                if labels[3+i].cget("text") == 0:
                    labels[3+i].configure(text=labels[2+i].cget("text"))
                    labels[2+i].configure(text=0)
                elif(labels[2+i].cget("text") == labels[3+i].cget("text")):
                    labels[3+i].configure(text=labels[3+i].cget("text")*2)
                    labels[2+i].configure(text=0)
            if labels[1+i].cget("text") != 0:
                if labels[2+i].cget("text") == 0:
                    labels[2+i].configure(text=labels[1+i].cget("text"))
                    labels[1+i].configure(text=0)
                elif(labels[1+i].cget("text") == labels[2+i].cget("text")):
                    labels[2+i].configure(text=labels[2+i].cget("text")*2)
                    labels[1+i].configure(text=0)
            if labels[0+i].cget("text") != 0:
                if labels[1+i].cget("text") == 0:
                    labels[1+i].configure(text=labels[0+i].cget("text"))
                    labels[0+i].configure(text=0)
                elif(labels[0+i].cget("text") == labels[1+i].cget("text")):
                    labels[1+i].configure(text=labels[1+i].cget("text")*2)
                    labels[0+i].configure(text=0)
            i = i + 4
    
    handle_color()
    root.update()

#ändert Labelfarbe anhand der Zahl
def handle_color():
    for label in labels:
        if(label.cget("text") == 1):
            label.configure(fg_color="cyan")
        elif(label.cget("text") == 2):
           label.configure(fg_color="light sea green")
        elif(label.cget("text") == 4):
           label.configure(fg_color="dodger blue")
        elif(label.cget("text") == 8):
           label.configure(fg_color="slate blue")
        elif(label.cget("text") == 16):
           label.configure(fg_color="dark slate blue")
        elif(label.cget("text") == 32):
           label.configure(fg_color="dark slate gray")
        elif(label.cget("text") == 64):
            label.configure(fg_color="tomato")
        elif(label.cget("text") == 128):
            label.configure(fg_color="orange")
        elif(label.cget("text") == 256):
            label.configure(fg_color="DarkGoldenrod4")
        elif(label.cget("text") == 512):
            label.configure(fg_color="maroon1")
        elif(label.cget("text") == 1024):
            label.configure(fg_color="maroon4")
        elif(label.cget("text") == 2048):
            label.configure(fg_color="purple4")
        else:
            label.configure(fg_color="white")

#startet spiel
def handle_start():
    root.title("2048")
    root.minsize(500,440)
    root.maxsize(500,440)
    root.config(background="white")
    root.bind("<KeyPress>", handle_key)

    text = customtkinter.CTkLabel(root, text="2048", font=("Arial",25),width=500,height=40)
    text.grid(row=0, column=0, columnspan=4, sticky="nsew")

    #inizialisierung spielfeld
    for i in range(4):
        for j in range(4):
            label = customtkinter.CTkLabel(master=root, text=0, fg_color="white",text_color="black",bg_color="white", font=("Arial",25),width=120,height=90, corner_radius=25)
            label.grid(row=i+1, column=j, padx=2, pady=2)
            labels.append(label)

    #spielanfang
    newnumber()
    newnumber()
    newnumber()
    newnumber()
    newnumber()
    handle_color()

    root.mainloop()


handle_start()
#written by Benjamin Wende
