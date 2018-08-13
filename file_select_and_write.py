import os
from tkinter import *

class FileHandler:
    @staticmethod
    def list_files(path):
        files = []
        for dir_path, dir_names, file_names in os.walk(path):
            files += [os.path.join(dir_path, filename) for filename in file_names]
        return files

    @staticmethod
    def filter_files(files, extension):
        filtered_files = []
        for file in files:
            if file[len(extension) * -1:] in extension:
                filtered_files.append(file)
        return filtered_files

    @staticmethod
    def save_filenames_to_file(filenames_to_write, file):
        with open(file, "w+") as f:
            for fn in filenames_to_write:
                f.write(fn + "\n")


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


class CheckboxGui2(Frame):
    chosen_files = []

    def __init__(self, root, path, extension, filename):
        Frame.__init__(self, root)
        self.root = root

        self.vsb = Scrollbar(self, orient="vertical")
        self.text = Text(self, width=120, height=50,
                         yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=False)

        files = FileHandler.filter_files(FileHandler.list_files(path), extension)
        i = 0
        for file in files:
            var1 = IntVar()
            cb = Checkbutton(self, text=file, variable=var1)
            self.chosen_files.append([file, var1])
            self.text.window_create("end", window=cb)
            self.text.insert("end", "\n")
            i += 1

        button = Button(self, text="Write", command=self.print_out)
        close_button = Button(self, text="Close", command=root.quit)
        button.pack()

        close_button.pack()
        self.pack(side="top", fill="both", expand=False)

        self.filename = filename
        self.master = root
        root.title("pyFilePathPrinter")

    def print_out(self):
        write_files = []
        for a in self.chosen_files:
            if a[1].get() == 1:
                write_files.append(a[0])
        FileHandler.save_filenames_to_file(write_files, self.filename)


def main():
    root1 = Tk()
    inp = GetUserInputGui(root1)
    root1.mainloop()
    root1.destroy()

    root3 = Tk()
    CheckboxGui2(root3, inp.path, inp.extension, inp.filename)
    root3.mainloop()

    # root2 = Tk()
    # CheckboxGui(root2, inp.path, inp.extension, inp.filename)
    # root2.mainloop()


if __name__ == "__main__":
    main()
