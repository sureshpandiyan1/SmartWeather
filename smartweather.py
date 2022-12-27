from tkinter import *

import contextlib
from smartweather_rtr import http_connc
from smartweather_db import cfgs

def half_screen(z,ww,hh):
        global w,h 
        w,h = z.winfo_screenwidth(),z.winfo_screenheight()
        z.geometry("{}x{}+{}+{}".format(ww, hh, int((w/2) - (ww/1.9)), int((h/2.2) - (hh/2))))



def splash_Screen():
    st= Tk()
    half_screen(st, 404, 243)
    st.overrideredirect(True)
    st.config(background="#fff")
    l = PhotoImage(file="weathersplash.png")
    z = Label(st, image=l, background="#fff")
    z.pack()
    z.after(3000,st.destroy)
    st.mainloop()

splash_Screen()


def m(m):
    for x in [int(m)]:
        if x > 0 and 27  > x:
            return "#ED0051"
        if x > 27 and 90 > x:
            return "#ED0000"
        elif str(x).startswith("-"):
            return "#1E75F7"

app = Tk()

app.title("SmartWeather")
app.resizable(0,0)
app.config(background="#FE7F00")

app.geometry("400x180")

half_screen(app, 400, 170)


h = []
def mm():
    ll = Label(app, text="Your Country Name: ", font=("Arial","15"), foreground="#fff", background="#FE7F00")
    ll.pack()
    ll.place(x=5,y=20)
    ls = Entry(app, width=30, font=("Arial","16"))
    ls.place(x=8, y=60, height=40)

    def k(): 

        h.append(ls.get())
        with open("country.txt","w") as mz:
            print(h[0], file=mz)
        ls.delete("0",END)
        app.after(1000, app.destroy())


    
    z = Button(app, command=k, text="just type above, then tap me!!", font=("Arial","16"), width=36, foreground="#fff", background="#000")
    z.pack(side="bottom")
    z.place(x=-20,y=120, height=50, anchor="nw")



# print()
try:
    with open("country.txt","r") as mmaa:
        l = http_connc("https://www.google.com/search?q={0}+weather".format(mmaa.read().strip()))
        l.get_data()

    if bool(cfgs().get_cfg("C","celusis")) == True:


        with contextlib.suppress(Exception):
            app.destroy()
            p = Tk()
            p.title("")
            p.geometry("200x180")

            p.resizable(0,0)

            p.iconbitmap("smartweather.ico")
            p.config(background=m(cfgs().get_cfg("C","celusis")))
            ll = Label(p, text=cfgs().get_cfg("C","celusis") + "°C", font=("arial","48","bold"), background=m(cfgs().get_cfg("C","celusis")), foreground="#fff")
            ll.pack()
            ll.place(x=24,y=44)
            lz = Label(p, text="Created By Suresh P | SmartWeather", background=m(cfgs().get_cfg("C","celusis")), foreground="#fff")
            lz.pack(side="bottom")
            p.mainloop()
except:
    mm()


app.mainloop()



