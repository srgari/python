import matplotlib.pyplot as plt, numpy as np
from tkinter import Tk, PhotoImage, Entry, Label
from PIL import ImageTk, Image


def espiral(entry):
    n = int(e.get())

    def s(n):
        import matplotlib.pyplot as plt
        x=[1]
        y=[0]
        c=0
        d=1
        for _ in range(n):
            y.append(y[-1]+(n-c))
            y.append(y[-1])
            x.append(x[-1])
            x.append(x[-1]+n-d) #avança
            c+=1
            d+=1
            y.append(y[-1]-(n-c))
            y.append(y[-1])
            x.append(x[-1])
            x.append(x[-1]-n+d) #retrocede
            d=d+1
            c = c+1
        y[0]=1
        
        return x[0:2*n],y[0:2*n]
    
    plt.clf()
    t=np.array(s(n))*3
    plt.plot(t[0], t[1])
    
    plt.savefig('espiral1.png')

    load = Image.open('espiral1.png')
    render = ImageTk.PhotoImage(load)
    img = Label(w, image = render)
    img.image = render
    img.place(x=0, y=100)    

w = Tk()
w.geometry('600x600')

titulo = Label(w, text = 'espiral!',)
titulo.place(x=0, y=0)
titulo.config(font=("Courier", 44))

# load = Image.open('espiral.png')
# render = ImageTk.PhotoImage(load)
# img = Label(w, image = render)
# img.image = render
# img.place(x=0, y=120)

e = Entry(w, width=50)
e.insert(0,'Digite o número de espirais')
e.place(x=0, y=80)


w.bind('<Return>', espiral)




w.mainloop()