import tkinter as tk
from tkinter import Menu, LabelFrame, Label, Entry, Button, Listbox, Scale, StringVar
import os
import subprocess
from tkinter import filedialog
import sys

def new_window():
    """Open a new application window."""
    subprocess.Popen([f"{sys.executable}", f"{__file__}"])

# Assume we have a global variable 'scan_data' that stores the current scan data as a string
scan_data = ''

def open_scan():
    """Open a scan from a file."""
    global scan_data  # Make sure we're modifying the global variable
    filepath = filedialog.askopenfilename()
    if not filepath:  # User cancelled the dialog
        return
    with open(filepath, 'r') as file:
        scan_data = file.read()

def save_scan():
    """Save the current scan to a file."""
    global scan_data  # Make sure we're using the global variable
    # If the current scan has not been saved before, call save_scan_as instead
    if not "existing_file_path":
        save_scan_as()
    else:
        filepath = "existing_file_path"  # Replace this with the actual file path
        with open(filepath, 'w') as file:
            file.write(scan_data)

def save_scan_as():
    """Save the current scan to a new file."""
    global scan_data  # Make sure we're using the global variable
    filepath = filedialog.asksaveasfilename()
    if not filepath:  # User cancelled the dialog
        return
    with open(filepath, 'w') as file:
        file.write(scan_data)


def quit_app(root):
    """Close the application."""
    root.quit()  # Or root.destroy(), depending on your needs


from tkinter import PhotoImage
from subprocess import Popen, PIPE
import shlex



def start_capture():
    # Define your command as a string
    cmd = "grgsm_livemon_headless"

    # Use shlex.split to handle the command string
    cmd_args = shlex.split(cmd)

    # Open a subprocess running the command
    process = Popen(cmd_args, stdout=PIPE, stderr=PIPE)

    # If you want to read from the process's output, you can use process.communicate() 

# Create the stop_capture function
def stop_capture():
    # TODO: Add code to stop the gr-gsm process
    pass

# Create the save_capture function
def save_capture():
    # TODO: Add code to save the current capture
    pass


def create_app():
    root = tk.Tk()
    root.geometry('800x600')
    root.title('GSM Capture')

    # Menu
    menubar = Menu(root)
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="New Window       Ctrl + N", command=new_window)
    file_menu.add_command(label="Open Scan        Ctrl + O", command=open_scan)
    file_menu.add_command(label="Save Scan        Ctrl + S", command=save_scan)
    file_menu.add_command(label="Save Scan as     Ctrl + Alt + S", command=save_scan_as)
    file_menu.add_command(label="Quit             Ctrl + Q", command=lambda: quit_app(root))
    menubar.add_cascade(label="File", menu=file_menu)

    # Edit Menu
    edit_menu = Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    menubar.add_cascade(label="Edit", menu=edit_menu)

    # View Menu
    view_menu = Menu(menubar, tearoff=0)
    view_menu.add_command(label="View 1")
    view_menu.add_command(label="View 2")
    menubar.add_cascade(label="View", menu=view_menu)

    # Help Menu
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Tutorial")
    menubar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menubar)

    # Configuration
    config_frame = LabelFrame(root, text='Configuration', padx=5, pady=5)
    config_frame.grid(row=0, column=0, sticky='nsew')

    Label(config_frame, text='Frequency').grid(row=0, column=0, sticky='e')
    Scale(config_frame, from_=8000000000, to=1990000000, orient='horizontal').grid(row=0, column=1, sticky='w')
    Label(config_frame, text='Gain Control').grid(row=1, column=0, sticky='e')
    Scale(config_frame, from_=0, to=100, orient='horizontal').grid(row=1, column=1, sticky='w')
    Label(config_frame, text='PPM Offset').grid(row=2, column=0, sticky='e')
    Scale(config_frame, from_=-150, to=150, orient='horizontal').grid(row=2, column=1, sticky='w')
    Label(config_frame, text='Radio Source Selection').grid(row=3, column=0, sticky='e')
    Entry(config_frame).grid(row=3, column=1, sticky='w')

    # Load the image file
    start_img = PhotoImage(file='start_capture.PNG').subsample(12, 12)
    stop_img = PhotoImage(file='stop_capture.PNG').subsample(12, 12)
    save_img = PhotoImage(file='save.PNG').subsample(12, 12) 

    # Create the button
    start_button = Button(config_frame, image=start_img, command=start_capture)
    start_button.image = start_img  # Keep a reference to prevent garbage collection
    start_button.grid(row=4, column=0, columnspan=1, sticky='ew')
    # Create the Stop Capture button
    stop_button = Button(config_frame, image=stop_img, command=stop_capture)
    stop_button.image = stop_img  # Keep a reference to prevent garbage collection
    stop_button.grid(row=4, column=1, columnspan=1, sticky='ew')

    # Create the Save Capture button
    save_button = Button(config_frame, image=save_img, command=save_capture)
    save_button.image = save_img  # Keep a reference to prevent garbage collection
    save_button.grid(row=4, column=2, columnspan=1, sticky='ew')

    # Ensure grid cells in configuration frame expand proportionally with frame resize
    config_frame.grid_columnconfigure(1, weight=1)

    # Display
    display_frame = LabelFrame(root, text='Display', padx=5, pady=5)
    display_frame.grid(row=0, column=1, sticky='nsew')

    Label(display_frame, text='Scope to display selected frequency').pack()
    Label(display_frame, text='Status').pack()
    Entry(display_frame).pack()

    Label(display_frame, text='Table of detected IMSI numbers and additional info').pack()
    Listbox(display_frame).pack(fill='both', expand=True)

    # Logs
    log_frame = LabelFrame(root, text='Logs', padx=2, pady=2)
    log_frame.grid(row=1, column=0, sticky='nsew')
    Listbox(log_frame).pack(fill='both', expand=True)

    # Map (placeholder, replace with actual map widget)
    map_frame = LabelFrame(root, text='Map', padx=5, pady=5)
    map_frame.grid(row=1, column=1, sticky='nsew')
    Label(map_frame, text='Map Placeholder').pack()

    # Ensure grid cells expand proportionally with window resize
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1) 
    root.mainloop()

if __name__ == "__main__":
    create_app()
