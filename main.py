import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x300")
label = ctk.CTkLabel(root, text="Hello, World!")
label.pack(pady=20)
button = ctk.CTkButton(root, text="Click Me", command=lambda: label.configure(text="Button Clicked!"))
button.pack(pady=10)
root.mainloop()

