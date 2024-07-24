from tkinter import Label, Tk
from time import strftime

window = Tk()
window.title("Digital Clock")
window.geometry("480x270")
window.configure(bg="black")
window.resizable(False,False)

clock_label = Label(window,bg="black",fg="lime",font=("Arial",50,"bold"),relief="flat")
clock_label.pack(pady=40)

def update_label():
    current_time = strftime('%I:%M:%S %p')
    clock_label.configure(text=current_time, fg="lime")
    clock_label.after(1000,update_label)
    
update_label()

window.mainloop()
