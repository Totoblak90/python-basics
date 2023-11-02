from tkinter import *

window = Tk()
window.title("Km/Miles converter")
window.config(padx=20, pady=20)


def calculate_miles():
    try:
        miles_to_km = round(float(miles_entry.get()) * 1.6, 5)
        km_values_label.config(text=miles_to_km)
        error_label.config(text="")
        error_label.grid_remove()
    except:
        km_values_label.config(text="NaN")
        error_label.config(text="Only numbers are accepted")
        error_label.grid(column=1, row=4)
        pass


miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_text_label = Label(text="Miles", padx=5, pady=5)
miles_text_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", padx=5, pady=5)
is_equal_to_label.grid(column=0, row=1)

km_values_label = Label(text=0, padx=5, pady=5)
km_values_label.grid(column=1, row=1)

km_text_label = Label(text="Km", padx=5, pady=5)
km_text_label.grid(column=2, row=1)

calculate_btn = Button(
    text="Calculate", command=calculate_miles, padx=5, pady=5)
calculate_btn.grid(column=1, row=3)

error_label = Label(text="", background="white", padx=5, pady=5)


window.mainloop()
