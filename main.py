from tkinter import *
import os

st=Tk()
st.title("Shutdown App")
st.geometry("450x500")
st.config(bg="lightblue")
sbutton=Button(st,text="Shutdown",bg="red",font=("Time New Roman",18,"bold"))
sbutton.place(x=150,y=50,height=70,width=150)
rbutton=Button(st,text="Restart",bg="blue",font=("Time New Roman",18,"bold"))
rbutton.place(x=150,y=200,height=70,width=150)
ubutton=Button(st,text="Sleep",bg="blue",font=("Time New Roman",18,"bold"))
ubutton.place(x=150,y=350,height=70,width=150)

st.mainloop()
