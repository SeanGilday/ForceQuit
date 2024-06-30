import customtkinter
from api import trackGames

def interface():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500x350")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="ForceQuit")
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="How many games?")
    entry1.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Enter", command=trackGames)
    button.pack(pady=12, padx=10)

    root.mainloop()