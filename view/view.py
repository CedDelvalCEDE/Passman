import tkinter as tk


class GUI:

    def __init__(self):
        self.inter: tk.Tk = tk.Tk()
        self.label: tk.Label = tk.Label(text="Hi, I'm Dehui. It's time to work", background="#CEDE82")
        self.inter.geometry(f'{self.inter.winfo_screenwidth()}x{self.inter.winfo_screenheight()}')
        self.label.pack(in_=self.inter)

    def main_loop(self):
        self.inter.mainloop()


if __name__ == '__main__':
    test = GUI()
    test.main_loop()
