import os
import tkinter as tk
from tkinter import messagebox, simpledialog

DEFAULT_PATH = "C:/default/path/file.txt"

def ask_user():
    # Ask user if they want to give custom path
    answer = messagebox.askyesno("File Path Input", 
                                 "Do you want to provide a custom file path?\n\n"
                                 "Yes = Provide Path\nNo = Use Default")
    
    if answer:  # User wants to give path
        while True:
            user_path = simpledialog.askstring("Custom File Path", "Enter file path:")
            
            if user_path is None:  # User cancelled
                messagebox.showinfo("Info", f"Using default path:\n{DEFAULT_PATH}")
                return DEFAULT_PATH

            if os.path.exists(user_path):
                messagebox.showinfo("Success", f"Valid path selected:\n{user_path}")
                return user_path
            else:
                retry = messagebox.askyesno("Invalid Path", 
                                            f"'{user_path}' is not valid.\n"
                                            "Do you want to try again?\n\n"
                                            "Yes = Retry\nNo = Use Default")
                if not retry:
                    messagebox.showinfo("Info", f"Using default path:\n{DEFAULT_PATH}")
                    return DEFAULT_PATH
    else:
        messagebox.showinfo("Info", f"Using default path:\n{DEFAULT_PATH}")
        return DEFAULT_PATH


# Main Tkinter setup
root = tk.Tk()
root.withdraw()  # Hide root window

final_path = ask_user()
print("Final chosen path:", final_path)
