# need to get the food API library to compare against.
# this will allow for me to check to see if what was entered was even a real food.
# if not then we can tell them that what was entered was not a food and that we can then
# default for them to just re-enter another food.
# this will allow for us to not even need a good food list.
# defering allows us to not worry as much about the contents of the database.

from edamem_api import check_food
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
    selected_pet = clicked.get()
    entered_food = food_entry.get().lower()

    app_id = "b48e160d"
    app_key = "411b578a05b06957191e6ab0f463c9f1	"

    is_recognized, food_data = check_food(entered_food, app_id, app_key)

    if is_recognized:
        # Check if the entered food is in the bad foods list
        if selected_pet in bad_foods and entered_food in bad_foods[selected_pet]:
            result_label.config(
                text=f"This food is bad for {selected_pet}s!", bootstyle="danger"
            )
        else:
            result_label.config(
                text=f"This food is safe for {selected_pet}s.", bootstyle="success"
            )
    elif is_recognized is False:
        result_label.config(
            text=f"{entered_food} is not a recognized food.", bootstyle="danger"
        )
    else:
        result_label.config(
            text="Error connecting to the Edamam API.", bootstyle="danger"
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
