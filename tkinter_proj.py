import tkinter as tk
import Wr

def transfer():
    data = label2.get()
    label2.delete(0, tk.END)
    Exemplar = Wr.Weather(x=data).start()
    adress = Exemplar
    
    with open(adress) as file:
        label3['text'] = file.read()
    return data

window = tk.Tk()
window.title('Weather_Report.001')
a,b = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry(f'{a}x{b}')
frame1 = tk.Frame(master=window)
frame2 = tk.Frame(master=window)

label1 = tk.Label(master=frame1,text='City name: ', width=15, relief='groove')
label1.pack(side=tk.LEFT)
label2 = tk.Entry(master=frame1, width=30, relief='groove')
label2.pack(side=tk.RIGHT)

but1 = tk.Button(master=frame2, command=transfer, width=30)
but1.pack()

label3 = tk.Label(master=frame2, height=60, width=30, relief='groove')
label3.pack()

frame1.pack()
frame2.pack()

window.mainloop()