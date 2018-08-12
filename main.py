from tkinter import Tk, Label, Button
class Gui:
    def __init__(self, master):
        self.master = master
        master.title("pyFilePathPrinter")

        self.label = Label(master, text="This is the pyFilePathPrinter")
        self.label.pack()
        a = [1, 2, 3]
        for numbers in a:
            self.label = Label(master, text = numbers)
            self.label.pack()

        self.greet_button = Button(master, text="Working button, executes a function", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Printed message!")

def main():
  root = Tk()
  TheGui = GUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()