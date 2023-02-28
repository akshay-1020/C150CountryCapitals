from tkinter import *
import random

root = Tk()
root.title("Country Game")
root.geometry("400x400")
root.configure(bg="#963810")

ibox = Entry(root)
ibox.place(relx=0.5, rely=0.15, anchor=CENTER)

ibox2 = Entry(root)
ibox2.place(relx=0.5, rely=0.25, anchor=CENTER)

df = Label(root, bg="#963810", fg="white")
df.place(relx=0.5, rely=0.45, anchor=CENTER)

df2 = Label(root, bg="#963810", fg="white")
df2.place(relx=0.5, rely=0.5, anchor=CENTER)

l = Label(root, bg="#963810", fg="white")
l.place(relx=0.5, rely=0.7, anchor=CENTER)

l2 = Label(root, bg="#963810", fg="white")
l2.place(relx=0.5, rely=0.8, anchor=CENTER)

c = []
c2 = []

def ac():
    u = ibox.get()
    c.append(u)
    df["text"] = "Country Name: " + str(c)
    u2 = ibox2.get()
    c2.append(u2)
    df2["text"] = "City Name: " + str(c2)
    
def pc():
    co = random.randint(0, len(c)-1)
    l["text"] = "Random Country: " + str(c[co])
    co2 = random.randint(0, len(c2)-1)
    l2["text"] = "Random City: " + str(c2[co2])
    
ib = Button(root, text="Display Country and City Name", command=ac)
ib.place(relx=0.5, rely=0.35, anchor=CENTER)

pb = Button(root, text="Is This Correct?", command=pc)
pb.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
