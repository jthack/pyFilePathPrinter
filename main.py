from tkinter import *

from file_list import FileHandler as fh


class GetUserInputGui:
    path = ''
    extension = ''
    filename = ''

    def __init__(self, master):
        self.master = master
        self.label = Label(master, text="Path to search:")
        self.label.pack()
        self.e1 = Entry(master)
        self.e1.pack()
        self.e1.delete(0, END)
        self.e1.insert(0, ".")

        self.label = Label(master, text="File extension to use:")
        self.label.pack()
        self.e2 = Entry(master)
        self.e2.pack()
        self.e2.delete(0, END)
        self.e2.insert(0, "yml")

        self.label = Label(master, text="Name of file to write the paths to:")
        self.label.pack()
        self.e3 = Entry(master)
        self.e3.pack()
        self.e3.delete(0, END)
        self.e3.insert(0, "test.txt")

        self.close_button = Button(master, text="OK", command=self.on_button)
        self.close_button.pack()

    def on_button(self):
        self.path = self.e1.get()
        self.extension = self.e2.get()
        self.filename = self.e3.get()
        self.master.quit()


class CheckboxGui:
    chosen_files = []

    def __init__(self, master, path, extension, filename):
        self.filename = filename
        self.master = master
        master.title("pyFilePathPrinter")
        self.label = Label(master, text="This is the pyFilePathPrinter")
        self.label.pack()
        files = fh.filter_files(fh.list_files(path), extension)
        for file in files:
            var1 = IntVar()
            self.Checkbutton = Checkbutton(master, text=file, variable=var1)
            self.chosen_files.append([file, var1])
            self.Checkbutton.pack()
        self.button = Button(master, text="Print", command=self.print_out)
        self.button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def print_out(self):
        write_files = []
        for a in self.chosen_files:
            if a[1].get() == 1:
                write_files.append(a[0])
        fh.save_filenames_to_file(write_files, self.filename)


def main():
    root1 = Tk()
    inp = GetUserInputGui(root1)
    root1.mainloop()
    root1.destroy()

    root2 = Tk()
    CheckboxGui(root2, inp.path, inp.extension, inp.filename)
    root2.mainloop()


if __name__ == "__main__":
    main()