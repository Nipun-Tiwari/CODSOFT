import tkinter as tk

def create_custom_button1(parent, text, command):
    # Define button styles
    button_normal = {"bg": "#E10600", "fg": "white", "font": ("Helvetica", 22), "relief": "flat"}
    button_hover = {"bg": "#45a049", "fg": "white", "font": ("Helvetica", 22), "relief": "flat"}

    # Create a button with the defined styles
    button = tk.Button(parent, text=text, command=command, **button_normal)

    # Bind events to the button
    button.bind("<Enter>", lambda event: button.config(**button_hover))
    button.bind("<Leave>", lambda event: button.config(**button_normal))

    return button
def create_custom_button2(parent, text, command):
    # Define button styles
    button_normal = {"bg": "#4681f4", "fg": "white", "font": ("Helvetica", 22), "relief": "flat"}
    button_hover = {"bg": "#55c2da", "fg": "white", "font": ("Helvetica", 22), "relief": "flat"}

    # Create a button with the defined styles
    button = tk.Button(parent, text=text, command=command, **button_normal)

    # Bind events to the button
    button.bind("<Enter>", lambda event: button.config(**button_hover))
    button.bind("<Leave>", lambda event: button.config(**button_normal))

    return button
