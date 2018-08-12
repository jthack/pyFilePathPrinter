from tkinter import *
class Gui:
    def __init__(self, master):
        self.master = master
        master.title("pyFilePathPrinter")

        self.label = Label(master, text="This is the pyFilePathPrinter")
        self.label.pack()
        a = [1, 2, 3]
        for numbers in a:
            #self.label = Label(master, text = numbers)
            #self.label.pack()
            var1 = IntVar()
            self.Checkbutton = Checkbutton(master, text=numbers, variable=IntVar())
            self.Checkbutton.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

def main():
  root = Tk()
  TheGui = Gui(root)
  root.mainloop()

if __name__ == "__main__":
  main()