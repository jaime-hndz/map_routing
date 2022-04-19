import openstreetmap
from tkinter import *
from tkhtmlview import *


root = Tk()
root.title("Map routing")
root.geometry('400x600')

html_label = HTMLLabel(root, html='<h1 style="color: dodgerblue; text-align: center"> Map routing </H1><p>El presente proyecto consiste en ingresar 2 nodos de la provincia Hermanas Mirabal y el algoritmo se encarga de encontrar la ruta mas optima entre estos puntos.</p> <h3>Sustentantes: </h3><ul><li>Francis Terreo</li><li>Jean Reyes</li><li>Enmanuel Santos</li><li>Yahel Hichez</li><li>Jeremy Herrera</li><li>Luis Marmol</li><li>Jaime Hernandez</li></ul>')
html_label.pack(fill="both", expand=True)

txt1 = Entry(root, font=("Arial",24))
txt1.pack()
txt2 = Entry(root, font=("Arial",24))
txt2.pack()



def limpiar():
    txt1.delete("0", "end")
    txt2.delete("0", "end")

def ejecutar():
    try:
        openstreetmap.main(int(txt1.get()),int(txt2.get()))
        link = HTMLLabel(root, html='<div style="text-align: center;"><a href="mapa.html" style="color: dodgerblue;">Ver mapa</a></div>')
        link.pack()
        limpiar()
    except Exception as e:
        print(e)
        popupmsg("Algo ha salido mal")

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

btn = Button(text="Ejecutar", command= ejecutar,font=("Arial",12), width=30, height=1)
btn.pack()
btnlimpiar = Button(text="Limpiar", command= limpiar,font=("Arial",12), width=30, height=1)
btnlimpiar.pack()



# openstreetmap.main(10,30)
root.mainloop();
