import Tkinter as tk
import tkMessageBox
import time

class tk_dd:
    def __init__(self):
        self.window = tk.Tk()
        self.choice = '1 Min','2 Mins','3 Mins'

    def select_mins(self):

        def change_dd(self):
            print def_set.get()
            select_ddval = def_set.get()
            if select_ddval:
                tval = int(select_ddval.split(' ')[0])
                print "System get reboots in {} mins".format(tval)
                time.sleep(tval)
            tkMessageBox.showinfo("Reboot Required","Reboot in few Seconds")

        #Label
        min_lbl = tk.Label(self.window,text="Reboot in",fg='blue')
        min_lbl.pack()
        #DropDown
        def_set = tk.StringVar(self.window)
        def_set.set("Pospond")
        dd = tk.OptionMenu(self.window,def_set,'10 Min','2 Mins','3 Mins',command=change_dd)
        print "dd value",
        dd.pack(side='left',padx='10',pady='10')
        #RadioButton
        v = tk.IntVar(value=1) # used to default selection of radio button (value 1python selected)
        tk.Radiobutton(self.window,text="Python",padx=20,variable=v,value=1).pack(anchor=tk.CENTER)
        tk.Radiobutton(self.window,text="Perl",padx=20,variable=v,value=2).pack(anchor=tk.W)
        #CheckBox
        tk.Checkbutton(self.window,padx = 20,text="python").pack()
        tk.Checkbutton(self.window,padx = 20, text="Ruby").pack()

        self.window.mainloop()

obj_tk_dd = tk_dd()
obj_tk_dd.select_mins()

