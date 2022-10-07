from tkinter import *
root=Tk()

mymenu=Menu(root)
root.config(menu=mymenu)

def fun1():
    print("this is new project")
def fun2():
    print("this is new ")
    root.quit()
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="New Project",command=fun1)
submenu.add_command(label="New",command=fun2 )

toolbar=Frame(root,bg="pink")
inbutton=Button(toolbar,text="crop")
inbutton.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)
statusbar=Label(root,text="this is status bar" ,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)
root.mainloop()
