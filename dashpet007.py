from tkinter import *
import ttkbootstrap as tb
from foods import bad_foods, good_foods

root = tb.Window(themename="vapor")
root.title("dashpet food safety calculator!")
root.geometry("500x350")

# label
my_label = tb.Label(text="Dashpet", font=("Roboto", 28), bootstyle="secondary")
my_label.pack(pady=20)


# FUNCTIONS
def compile_results():
    # Get the selected pet and entered food
    selected_pet = clicked.get()
    entered_food = food_entry.get().lower()

    # Check if the entered food is in the dictionary of bad foods for the selected pet
    if selected_pet in bad_foods and entered_food in bad_foods[selected_pet]:
        result_label.config(
            text=f"This food is bad for {selected_pet}s!", bootstyle="danger"
        )
    else:
        result_label.config(
            text=f"This food is safe for {selected_pet}s.", bootstyle="success"
        )


def selected():
    my_label = tb.Label(root, text=clicked.get())
    my_label.pack()


# Lists
options = ["Cat", "Dog"]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack(pady=10)

# Entry box for food
food_label = tb.Label(text="Enter Food:")
food_label.pack()
food_entry = Entry(root)
food_entry.pack(pady=10)

# Button
my_button = tb.Button(
    text="Compile Results", bootstyle="primary", command=compile_results
)
my_button.pack(pady=20)

# Result label to display if the food is good or bad for the selected pet
result_label = tb.Label(text="", bootstyle="info")
result_label.pack()

root.mainloop()
