from tkinter import *
FONT = ("Arial", 20, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

def calculate():
   miles = float(miles_input.get())
   km = round(miles * 1.6)
   label_4.config(text= f"{km}")

label_1 = Label(text="is equal to", font=FONT)
label_1.grid(column=0, row=1)

label_2 = Label(text="Miles", font=FONT)
label_2.grid(column=3, row=0)
label_2.config(padx=10, pady=10)

label_3 = Label(text="km", font=FONT)
label_3.grid(column=3, row=1)

label_4 = Label(text="0", font=FONT)
label_4.grid(column=1, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

button = Button(text="Calculate", width=10, command=calculate)
button.grid(column=1, row=3)








window.mainloop()