import tkinter as tk
from tkinter import Menu, LabelFrame, Label, Entry, Button, Listbox, Scale, StringVar

def create_app():
    root = tk.Tk()
    root.geometry('800x600')
    root.title('GSM Capture')

    # Menu
    menubar = Menu(root)
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save as")
    menubar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menubar)

    # Configuration
    config_frame = LabelFrame(root, text='Configuration', padx=5, pady=5)
    config_frame.pack(fill='both', expand='yes', side='left')

    Label(config_frame, text='Frequency').pack()
    Entry(config_frame).pack()
    Label(config_frame, text='Gain Control').pack()
    Entry(config_frame).pack()
    Label(config_frame, text='PPM Offset').pack()
    Entry(config_frame).pack()
    Label(config_frame, text='Radio Source Selection').pack()
    Entry(config_frame).pack()

    Button(config_frame, text='Start Capture').pack(fill='x')
    Button(config_frame, text='Stop Capture').pack(fill='x')
    Button(config_frame, text='Save Capture').pack(fill='x')

    # Display
    display_frame = LabelFrame(root, text='Display', padx=5, pady=5)
    display_frame.pack(fill='both', expand='yes', side='right')

    Label(display_frame, text='Scope to display selected frequency').pack()
    Label(display_frame, text='Status').pack()
    Entry(display_frame).pack()

    Label(display_frame, text='Table of detected IMSI numbers and additional info').pack()
    Listbox(display_frame).pack(fill='both', expand=True)

    # Logs
    log_frame = LabelFrame(root, text='Logs', padx=5, pady=5)
    log_frame.pack(fill='both', expand='yes', side='bottom')
    Listbox(log_frame).pack(fill='both', expand=True)

    # Map (placeholder, replace with actual map widget)
    map_frame = LabelFrame(root, text='Map', padx=5, pady=5)
    map_frame.pack(fill='both', expand='yes', side='bottom')
    Label(map_frame, text='Map Placeholder').pack()

    root.mainloop()

if __name__ == "__main__":
    create_app()
