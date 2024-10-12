from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def Calculate():
    miles_to_convert = int(miles.get())
    converted_value = miles_to_convert * 1.609344
    kilometer.config(text=converted_value)

is_equal_to = Label(text="is equal to", font=("Courier", 15))
is_equal_to.grid(column=0, row=1)

miles = Entry(width=10)
miles.grid(column=1, row=0)

kilometer = Label(text="0", font=("Courier", 18))
kilometer.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=Calculate)
calculate_button.grid(column=1, row=2)

miles_label = Label(text="Miles", font=("Courier", 15))
miles_label.grid(column=2, row=0)

Km_label = Label(text="Km", font=("Courier", 15))
Km_label.grid(column=2, row=1)




window.mainloop()
