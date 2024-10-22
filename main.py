from tkinter import *
import os
def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def sign_out():
    os.system("shutdown -l")

def switch_user():
    os.system("tsdiscon")


st=Tk()
st.title("Shutdown App")
st.geometry("470x500")
st.config(bg="lightblue")
sbutton=Button(st,text="Shutdown",bg="red",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="hand2",command=shutdown)
sbutton.place(x=150,y=40,height=65,width=150)
rbutton=Button(st,text="Restart",bg="#3498db",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="hand2",command=restart)
rbutton.place(x=150,y=125,height=65,width=150)
spbutton=Button(st,text="Sleep",bg="#3498db",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="hand2",command=sleep)
spbutton.place(x=150,y=210,height=65,width=150)
swpbutton=Button(st,text="Switch User",bg="#3498db",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="hand2",command=switch_user)
swpbutton.place(x=150,y=295,height=65,width=150)
sopbutton=Button(st,text="Sign Out",bg="#3498db",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="hand2",command=sign_out)
sopbutton.place(x=150,y=380,height=65,width=150)

st.mainloop()
