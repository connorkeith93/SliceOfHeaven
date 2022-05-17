#This pizza ordering app will allow you to input your personal information,
#then order the type of pizza you would like as well as a drink

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#Creates and Labels Window
pizza = Tk()
pizza.geometry("800x600")
pizza.title ("Slice Of Heaven - Ordering App")

#Labels and input boxes to obtain user info
name_label = Label(pizza, text="Name for order: ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=30)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text="Address for order: ")
address_label.grid(row=1, column=0)

address_entry = Entry(pizza, width=30)
address_entry.grid(row=1, column=1)

emailaddress_label = Label(pizza, text = "Email address for order: ")
emailaddress_label.grid(row=2, column=0)

emailaddress_entry = Entry(pizza, width=30)
emailaddress_entry.grid(row=2, column=1)

#Making a list of toppings for pizzas
my_pizza_list = ["Cheese", "Pepperoni", "Sausage", "Onions", "Mushrooms", "Olives", "Tomatoes", "Pineapple"]

#Choose multiple toppings from list created
# Changes background color to black, foreground is white
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="black", fg="white")
pizza_list.grid(row=4, column = 1)

#Adds Toppings into the List
for item in my_pizza_list:
    pizza_list.insert(0, item)

#Allows current selection of pizza toppings to be added and set to be output
def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text = "Your Pizza: " + "\n" + result)

add_lbl = Label(pizza, text = "")
add_lbl.grid(row=8, column =1)


#Creates a button to add the pizza the user creates
add_button= Button(pizza, text="Add Pizza", command = add_pizza)
add_button.grid(row=5, column=1)

#Defines checkout and outputs user Info when hitting the checkout button
def checkout():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text="Name: " + text1)
    new_lbl.grid(row=5, column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text="Address: " + text2)
    new_lbl2.grid(row=6, column=2)

    text3 = emailaddress_entry.get()
    new_lbl3 = Label(pizza, text="Email Address: " + text3)
    new_lbl3.grid(row=7, column=2)



#Creates a checkout button
checkout_button = Button(pizza, text="Checkout Order", command=checkout)
checkout_button.grid(row=6, column=1)

def deletepizza():
    pizza_list.delete(0,8)

#Creates a delete button
del_button = Button(pizza, text = "Delete Pizza Created", command = deletepizza)
del_button.grid(row=7, column=1)

#Importing Picture of Pizza
img = (Image.open("Pizza.png"))

#Resize Image
resized_image = img.resize((175,175), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

#Outputs Image
pic_lbl = Label(pizza, image=new_image)
pic_lbl.grid(row=1, column=10)

#Adding confirmation Window for Exit button
def exit_confirm():
    answer = messagebox.askyesno("Exit Confirmation", "Are you sure you want to leave?")
    if answer == 1:
        pizza.destroy()
    else:
        return

#Creating an exit button
exit_button = Button(pizza, text="Exit app", command = exit_confirm)
exit_button.grid(row=13,column=0)


pizza.mainloop()