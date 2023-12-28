from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image

# GUI


class Widget:
    def __init__(self):
        self.root = CTk()
        set_appearance_mode("system")
        self.root.title('Nemo')
        self.root.geometry('400x450')

        def togglemode():
            current_bg = self.root.cget("bg")
            if current_bg == "gray14":
                set_appearance_mode("light")
            else:
                set_appearance_mode("dark")

        photo = ImageTk.PhotoImage(file='Data//Nemo_logo.png')
        self.button = Button(master=self.root, image=photo,
                             command=self.clicked).pack(pady=80)
        night_btn = ImageTk.PhotoImage(Image.open('Data//Dark_Light.png'))
        self.my_button = Button(
            self.root, image=night_btn, command=togglemode, borderwidth=0)
        self.my_button.pack(side='right')

        self.root.mainloop()

    def clicked(self):
        from Main_Nemo import ThisMain
        ThisMain()


if __name__ == '__main__':
    widget = Widget()
