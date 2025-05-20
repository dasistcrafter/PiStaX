from tkinter import *

def settigsboxtrigger():
    print("settigsboxtriggert")

def terminalboxtrigger():
    print("terminalboxtriggert")

def toolboxtirgger():
    print("toolboxtriggert")

def taskmanagerboxtrigger():
    print("taskmanagerboxtrigger")

#img
tkFenster = Tk()
tkFenster.geometry("240x240")
tkFenster.title("240px*240px")
tkFenster.configure(bg="black")


imagesettings = PhotoImage(file="Img/button-5029978_640.gif")
imageterminal = PhotoImage(file="")
imagetoolbox = PhotoImage(file="")
imagetaskmanager = PhotoImage(file="")

#settingsbutton
labelSettingbox = Button(master=tkFenster, image=imagesettings, command=settigsboxtrigger)
labelSettingbox.place(x=5, y=5, width=55, height=55)

#terminalbutton
labelterminalbox = Button(master=tkFenster, text="Terminal", fg="#008000", bg="gray", font=("Arial", 8), command=terminalboxtrigger)
labelterminalbox.place(x=65, y=5, width=55, height=55)

#toolboxtrigger
labeltoolbox = Button(master=tkFenster, text="Tools", fg="black", bg="#cc0052", font=("Arial", 8), command=toolboxtirgger)
labeltoolbox.place(x=125, y=5, width=55, height=55)

#Taskmanager
labeltaskmanagerbox = Button(master=tkFenster, text="TaskMNG", fg="#008000", bg="gray", font=("Arial", 8), command=taskmanagerboxtrigger)
labeltaskmanagerbox.place(x=185, y=5, width=55, height=55)

tkFenster.mainloop()
