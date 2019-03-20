import Tkinter as tk
import tkMessageBox
import time
window = tk.Tk(300*200)
window.title("Counter")

counter = 0
def counter_check():
    global counter
    counter+=1
    lbl.config(text=str(counter))
    lbl.after(1000,counter_check)

def wait_time():
    time.sleep(10)
    tkMessageBox.showinfo("Wait Tab","Counter will get start in few seconds")
    time.sleep(4)

lbl = tk.Label(window, fg='BLUE')
lbl.pack()
counter_check()
btn = tk.Button(window,text='Stop',command = wait_time)
#btn = tk.Button(window,text='Stop',command = window.destroy)
btn.pack()
window.mainloop()
