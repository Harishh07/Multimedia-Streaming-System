import tkinter

import os


window = tkinter.Tk()
window.title("Brodcasting | Streaming App")
window.configure(background='black')

img = tkinter.PhotoImage(file="img.png")
label = tkinter.Label(image=img)
label.place(x=0, y=0)  


l1 = tkinter.Label(window,text = "\n\nBROADCASTING/STREAMING SERVICES", font=("Arial Bold",30),fg="white",bg="black").pack()
l2 = tkinter.Label(window,text = "\n1) Audio Stream/Live Broadcast",font=("Oxygen Bold",17),fg="grey",bg="black").pack()
l3 = tkinter.Label(window,text = "\n2) Video (1080p 30FPS) Stream/Live Broadcast\n",font=("Oxygen Bold",17),fg="grey",bg="black").pack()
l4 = tkinter.Label(window,text = "3) Live Video Conferencing Streaming System\n",font=("Oxygen Bold",17),fg="grey",bg="black").pack()


def server1():
 tkinter.Label(window,text="Streaming Audio...",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.39, rely =0.6)
 os.system('python server1.py')
 tkinter.Label(window,text="Audio Stream Ended",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.344, rely =0.6)
 tkinter.Label(window,text="Thanks for using! Cheers:)",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.3, rely =0.7)

def server2():
 tkinter.Label(window,text="Streaming Video...",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.39, rely =0.6)
 os.system('python server2.py')
 tkinter.Label(window,text="Video Stream Ended",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.344, rely =0.6)
 
 tkinter.Label(window,text="Thanks for using! Cheers:)",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.3, rely =0.7)


def server3():
 tkinter.Label(window,text="Streaming Video...",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.39, rely =0.6)
 os.system('python server3.py')
 tkinter.Label(window,text="Video Stream Ended",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.344, rely =0.6)
 
 tkinter.Label(window,text="Thanks for using! Cheers:)",font=("Arial Bold",30),fg="white",bg="black").place(relx = 0.3, rely =0.7)


bt= tkinter.Button(window,text="One",command = server1,font=("Oxygen Bold",17)).place(relx = 0.41, rely =0.5)
bt1= tkinter.Button(window,text="Two",command = server2,font=("Oxygen Bold",17)).place(relx = 0.47, rely =0.5)
bt1= tkinter.Button(window,text="Three",command = server3,font=("Oxygen Bold",17)).place(relx = 0.53, rely =0.5)

'''
bt.grid(column=1,row=3)
bt1.grid(column=2,row=3)
'''

'''
rad1= tkinter.Radiobutton(window,text="Audio Streaming",value=1,font=("Comic Sans MS",17)) 
rad2= tkinter.Radiobutton(window,text="Video Streaming",value=2,font=("Lucida Sans Bold",17))


rad1.grid(column=1,row=4)
rad2.grid(column=2,row=4)
'''

window.geometry('1220x780')
window.mainloop()