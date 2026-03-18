import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


        # ПРАВИЙ фрейм (одразу в self, без "зайвого" контейнера)
        self.right_frame = customtkinter.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")


class MyButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.pack(padx=10, pady=10)

    def button_callback(self):
        print("button pressed")

class MyLabelFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(self, text="Я на 2 рядки 😎", padx=10)
        self.label.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        self.label.pack(expand=True)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")


        self.label_frame = MyLabelFrame(self)
        self.label_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.button_frame = MyButtonFrame(self)
        self.button_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ew")


    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()