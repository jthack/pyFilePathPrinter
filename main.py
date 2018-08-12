from tkinter import *
from file_list import FileHandler as fh


class Gui:
    chosen_files = []

    def __init__(self, master):
        self.master = master
        master.title("pyFilePathPrinter")
        self.label = Label(master, text="This is the pyFilePathPrinter")
        self.label.pack()
        files = fh.filter_files(fh.list_files('.'), 'py')
        for file in files:
            var1 = IntVar()
            self.Checkbutton = Checkbutton(master, text=file, variable=var1)
            self.chosen_files.append([file, var1])
            self.Checkbutton.pack()
        self.button = Button(master, text="Print", command=self.PrintOut)
        self.button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def PrintOut(self):
        for a in self.chosen_files:
            if a[1].get() == 1:
                print(a[0])
def main():
  root = Tk()
  TheGui = Gui(root)
  root.mainloop()

if __name__ == "__main__":
  main()