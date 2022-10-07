from tkinter import *
class myfun:
    def __init__(self,roott):
        frame=Frame(roott)
        frame.pack()
        self.okbutton=Button(frame,text="Ok",command=self.okbuttonn)
        self.okbutton.pack()
        self.cancelbutton = Button(frame, text="cancel", command=self.cancelbuttonn)
        self.cancelbutton.pack()
        self.quitbutton = Button(frame, text="quit", command=frame.quit)
        self.quitbutton.pack()

    def okbuttonn(self):
        print("clicked")
    def cancelbuttonn(self):
        print("canceled")

root=Tk()
obj=myfun(root)
root.mainloop()