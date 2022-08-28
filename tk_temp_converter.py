import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root our window and set demensions
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('325x80')
root.resizable(False, False)

# here we establish our equation for conversion
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Creates the frame from our tkinter import 
frame = ttk.Frame(root)


# Establishes our field range for our options
options = {'padx': 5, 'pady': 5}

# creating our temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# creating our temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# creating our convert button
def convert_button_clicked():
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# creating result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and showing it
frame.grid(padx=10, pady=10)


# Now establishing our start loop for the app
root.mainloop()