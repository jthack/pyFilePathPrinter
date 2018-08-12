from tkinter import *
from file_list import FileHandler as fh


class Gui:
    def __init__(self, master):
        self.master = master
        master.title("pyFilePathPrinter")

        self.label = Label(master, text="This is the pyFilePathPrinter")
        self.label.pack()
        files = fh.filter_files(fh.list_files('.'), 'py')
        for file in files:
            #self.label = Label(master, text = numbers)
            #self.label.pack()
            var1 = IntVar()
            self.Checkbutton = Checkbutton(master, text=file, variable=IntVar())
            self.Checkbutton.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

def main():
  root = Tk()
  TheGui = Gui(root)
  root.mainloop()

if __name__ == "__main__":
  main()