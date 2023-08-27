from tkinter import *
# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

ds=[100,97,96,93,100,91,90,89,88,100]
cn=[95,100,94,92,91,100,95,99,89,100]
cc=[99,88,100,86,93,100,97,100,98,96]
apt=[100,85,84,87,82,86,84,95,96,100]
eng=[96,94,100,97,95,100,94,91,95,100]
hin=[100,98,94,97,96,92,100,88,89,100]
fin=[96,98,100,87,88,92,94,100,99,96]
fswd=[100,100,95,96,94,87,82,84,100,89]

name=['Atish','sneha','varun','kartik','vinod',
      'juned','saif','nabil','Salman','janvi']

win=Tk()
win.geometry('390x250')
L1=Label(win,text="-: Top 10 Students Marks :-",font='bold').pack(side=TOP)

def DS():
      perl=[]
      for i in ds:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Data Science: ",per)
      plt.figure(figsize=(10,5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Data Science")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def CN():
      perl = []
      for i in cn:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Computer Network: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Computer Network")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def CC():
      perl = []
      for i in cc:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Cloud Computing: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Cloud Computing")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def APT():
      perl = []
      for i in apt:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Aptitude: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Aptitude")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def ENG():
      perl = []
      for i in eng:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("English: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("English")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def HIN():
      perl = []
      for i in hin:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Hindi: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Hindi")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def FIN():
      perl = []
      for i in fin:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Financial: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Financial")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()

def FSWD():
      perl = []
      for i in fswd:
            per = "%.2f" % (i / 30 * 100)
            perl.append(float(per))
      print("Full Stack Web Developer: ",per)
      plt.figure(figsize=(10, 5))
      plt.scatter(x=name, y=ds, c=perl, cmap="cool")
      plt.colorbar(label="marks", orientation="horizontal")
      plt.title("Full Stack Web Developer")
      plt.xlabel("Student")
      plt.ylabel("marks")
      plt.show()


B1=Button(win,text="Data Science", command=DS).place(x=20, y=70)
B2=Button(win,text="Comp Netwr", command=CN).place(x=110, y=70)
B3=Button(win,text="Cloud Comp", command=CC).place(x=200, y=70)
B4=Button(win,text="Aptitude", width=10, command=APT).place(x=290, y=70)
B5=Button(win,text="English", width=10, command=ENG).place(x=20, y=140)
B6=Button(win,text="Hindi",width=10, command=HIN).place(x=110, y=140)
B7=Button(win,text="Financial", width=10, command=FIN).place(x=200, y=140)
B8=Button(win,text="FSWD",width=10, command=FSWD).place(x=290, y=140)

win.mainloop()
