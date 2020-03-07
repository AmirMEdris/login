# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:06:55 2020

@author: Amir Edris
"""

import tkinter as tk
import os
wificonnect=0
domainjoin=0
custominstall=0
declutter=0
h = 1100
w = 1300
#def custominstallsetup():
    
def domainjoinsetup():
    djsw=tk.Tk()
    
    djsw.mainloop()
#def connectwifisetup():
    
#def decluttersetup():
def option1submit():
    ow.destroy
    if domainjoin==1:
        domainjoinsetup()
        
    


def option1windowsetup():
    oh=750
    oiw=900
    ow= tk.Tk()
    
    wificonnectlabel=tk.Label(ow,text='connect to wifi')
    wificonnectlabel.grid(row=0,column=1)
    
    wificonnectcheckbox=tk.Checkbutton(ow,variable=wificonnect)
    wificonnectcheckbox.grid(row=0,column =2)
    
    domainjoinlabel=tk.Label(ow,text='automatic domain join')
    domainjoinlabel.grid(row=3,column=1)
    
    domainjoincheckbox=tk.Checkbutton(ow,variable=domainjoin)
    domainjoincheckbox.grid(row=3,column =2)
    
    custominstallersetuplabel=tk.Label(ow,text='install applications')
    custominstallersetuplabel.grid(row=2,column=1)
    
    custuminstallersetupcheckbox=tk.Checkbutton(ow,variable=custominstall)
    custuminstallersetupcheckbox.grid(row=2,column =2)
    
    declutterlabel=tk.Label(ow,text='remove windows store items')
    declutterlabel.grid(row=1,column= 1)
    
    decluttercheckbox=tk.Checkbutton(ow,variable=declutter)
    decluttercheckbox.grid(row=1,column =2)
    
    submitbutton= tk.Button(ow,text='submit',command=option1submit)
    submitbutton.grid(row=4,column=2)
    ow.mainloop()
root= tk.Tk()

canvas = tk.Canvas(root,height=h,width = w,bg='cyan')
canvas.place(relheight=1,relwidth=1)

title_label = tk.Label(canvas, font=60,fg='orange',bg='cyan',text = 'SEiTup')
title_label.place(relx=0.5,rely=0.1,anchor='n')

mainmenuframe= tk.Frame(canvas)
mainmenuframe.place(relx=0.5,rely=0.3,anchor='n',relheight=0.5,relwidth=0.9)

option1=tk.Button(mainmenuframe,text='make an all-in-one pc setup exe',command = option1windowsetup)
option1.place(relx=0.5,rely=0.1,anchor='n')
root.mainloop()
