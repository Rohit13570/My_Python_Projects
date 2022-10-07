from tkinter import *
root=Tk()

mymenu=Menu(root)
root.config(menu=mymenu)

def fun1():
    print("this is new project")
def fun2():
    print("this is new ")
def fun3():
    print("this is new scratch")
def fun4():
    print("this is new open")
def fun5():
    print("this is save as")
def fun6():
    root.quit()
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="New Project",command=fun1)
submenu.add_command(label="New",command=fun2 )
submenu.add_separator()
submenu.add_command(label="New scratch",command=fun3)
submenu.add_command(label="open",command=fun4)
submenu.add_separator()
submenu.add_command(label="save as",command=fun5)
submenu.add_command(label="exit",command=fun6)

submenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=submenu)
submenu.add_command(label="undo typing")
submenu.add_command(label="redo")
submenu.add_separator()
submenu.add_command(label="cut")
submenu.add_command(label="copy")
submenu.add_command(label="copy as plaintext")

submenu=Menu(mymenu)
mymenu.add_cascade(label="view",menu=submenu)
submenu.add_command(label="Tools windows")
submenu.add_command(label="Appeareance")
submenu.add_separator()
submenu.add_command(label="Quick definition")
submenu.add_command(label="Quick type definition")
submenu.add_command(label="Parameter info")

submenu=Menu(mymenu)
mymenu.add_cascade(label="navigate",menu=submenu)
submenu.add_command(label="Back")
submenu.add_command(label="forward")
submenu.add_separator()
submenu.add_command(label="Nsearch everywhere")
submenu.add_command(label="class")
submenu.add_command(label="file")

submenu=Menu(mymenu)
mymenu.add_cascade(label="code",menu=submenu)
submenu.add_command(label="overide method")
submenu.add_command(label="implement method")
submenu.add_separator()
submenu.add_command(label="generate")
submenu.add_command(label="code completion")
submenu.add_separator()
submenu.add_command(label="inspect")

root.mainloop()