import tkinter as tk
from tkinter import ttk
import Wr

data_dict = {
    'current forecast':'current', 
    '5 days forecast':'5 days'
    }

def transfer():
    data = label2.get()
    data_x = data_dict[combox1.get()]
    Exemplar = Wr.Weather(data, mode=data_x).giveforecast()
    if data_x == 'current':
        label3['text'] = f'{Exemplar[0]}C° {Exemplar[1]}'
    if data_x == '5 days':
        label3['text'] = '\n'.join((f'{i}C° {k}' for i, k in Exemplar))
def save():
    data_x = data_dict[combox1.get()]
    data = label2.get()
    save_data = Wr.Save()
    if data_x == 'current':
        save_data.save_result(city=data, result=label3['text'])
    if data_x == '5 days':
        save_data.save_result(city=data, result=label3['text'])
            
window = tk.Tk()
window.title('Weather_Report.002')
a,b = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry(f'{a}x{b}')
frame1 = tk.Frame(master=window)
frame2 = tk.Frame(master=window)
frame3 = tk.Frame(master=window)

label1 = tk.Label(master=frame1,text='City name: ', width=15, relief='groove')
label1.pack(side=tk.LEFT)

label2 = tk.Entry(master=frame1, width=30, relief='groove')
label2.pack(side=tk.RIGHT)

but1 = tk.Button(master=frame2, text='Submit', command=transfer, width=15)
but1.pack()

combox1 = ttk.Combobox(master=frame2, values=["current forecast", "5 days forecast"], width=15)
combox1.pack()

but2 = tk.Button(master=frame3, text='Save', command=save, width=30)
but2.pack()

label3 = tk.Label(master=frame3, height=50, width=30, relief='groove')
label3.pack()

frame1.pack()
frame2.pack()
frame3.pack()

window.mainloop()
