from tkinter import *
import datetime

"""


"""

root = Tk()

root.title("Metric hours calculator")

def apply_default_values():
	# Default entry values
	day_1_in.insert(0, 0.0)
	day_2_in.insert(0, 0.0)
	day_3_in.insert(0, 0.0)
	day_4_in.insert(0, 0.0)
	day_5_in.insert(0, 0.0)
	day_6_in.insert(0, 0.0)
	day_7_in.insert(0, 0.0)

	day_1_out.insert(0, 0.0)
	day_2_out.insert(0, 0.0)
	day_3_out.insert(0, 0.0)
	day_4_out.insert(0, 0.0)
	day_5_out.insert(0, 0.0)
	day_6_out.insert(0, 0.0)
	day_7_out.insert(0, 0.0)

# Button functions

def button_clear():
	# Clears insert boxes
	day_1_in.delete(0, END)
	day_2_in.delete(0, END)
	day_3_in.delete(0, END)
	day_4_in.delete(0, END)
	day_5_in.delete(0, END)
	day_6_in.delete(0, END)
	day_7_in.delete(0, END)

	day_1_out.delete(0, END)
	day_2_out.delete(0, END)
	day_3_out.delete(0, END)
	day_4_out.delete(0, END)
	day_5_out.delete(0, END)
	day_6_out.delete(0, END)
	day_7_out.delete(0, END)

	apply_default_values()

def button_calculate():
	# Gets data from entries, runs calculations

	def hours_sum():
		# Returns number of hours remaining as int

		sum_list = []

		time_remaining1 = float(day_1_out.get()) - float(day_1_in.get())
		time_remaining2 = float(day_2_out.get()) - float(day_2_in.get())
		time_remaining3 = float(day_3_out.get()) - float(day_3_in.get())
		time_remaining4 = float(day_4_out.get()) - float(day_4_in.get())
		time_remaining5 = float(day_5_out.get()) - float(day_5_in.get())
		time_remaining6 = float(day_6_out.get()) - float(day_6_in.get())
		time_remaining7 = float(day_7_out.get()) - float(day_7_in.get())

		sum_list.append(time_remaining1)
		sum_list.append(time_remaining2)
		sum_list.append(time_remaining3)
		sum_list.append(time_remaining4)
		sum_list.append(time_remaining5)
		sum_list.append(time_remaining6)
		sum_list.append(time_remaining7)

		return int(sum(sum_list))

	def text_output():
		# Responds to user input with overtime

		if hours_sum() > 40:
			return str(f"{abs(hours_sum() - 40)} hours of overtime.\n")
		elif hours_sum() < 80:
			return str(f"{hours_sum() - 40} hours remaining.\n")
		elif hours_sum() == 40:
			return "You have exactly 40 hours!"
		else:
			print("Output is not working.")

	def move_to_screen():
		# Display output on 
		my_results.insert(END, text_output())

	move_to_screen()

def button_save():
	# Formats and writes str to textfile
	db_entry = []

	day_1 = [day_1_in.get(), day_1_out.get()]
	day_2 = [day_2_in.get(), day_2_out.get()]
	day_3 = [day_3_in.get(), day_3_out.get()]
	day_4 = [day_4_in.get(), day_4_out.get()]
	day_5 = [day_5_in.get(), day_5_out.get()]
	day_6 = [day_6_in.get(), day_6_out.get()]
	day_7 = [day_7_in.get(), day_7_out.get()]

	week = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]

	db_entry.append(week)

	my_date = datetime.datetime.now()

	with open('punchcard_db.txt', 'w') as f:
		entry_str = str(db_entry)
		f.write(f"{my_date}:{entry_str}\n")

# Labels (Row 1)

day1Label = Label(root, text="Day 1")
day2Label = Label(root, text="Day 2")
day3Label = Label(root, text="Day 3")
day4Label = Label(root, text="Day 4")
day5Label = Label(root, text="Day 5")
day6Label = Label(root, text="Day 6")
day7Label = Label(root, text="Day 7")

# Text boxes

day_1_in = Entry(root, width=5, borderwidth=3)
day_2_in = Entry(root, width=5, borderwidth=3)
day_3_in = Entry(root, width=5, borderwidth=3)
day_4_in = Entry(root, width=5, borderwidth=3)
day_5_in = Entry(root, width=5, borderwidth=3)
day_6_in = Entry(root, width=5, borderwidth=3)
day_7_in = Entry(root, width=5, borderwidth=3)

day_1_out = Entry(root, width=5, borderwidth=3)
day_2_out = Entry(root, width=5, borderwidth=3)
day_3_out = Entry(root, width=5, borderwidth=3)
day_4_out = Entry(root, width=5, borderwidth=3)
day_5_out = Entry(root, width=5, borderwidth=3)
day_6_out = Entry(root, width=5, borderwidth=3)
day_7_out = Entry(root, width=5, borderwidth=3)

# Text/results

my_results = Text(root, width=20, height=24, borderwidth=3)

# Buttons

button_clear = Button(root, text="Clear", padx=2, pady=2, command=button_clear)
button_calculate = Button(root, text="Calculate", padx=2, pady=2, command=button_calculate)
button_save = Button(root, text="Save", padx=2, pady=2, command=button_save)

# Grid layout

day1Label.grid(row=0, column=0, padx=5, pady=5)
day2Label.grid(row=1, column=0, padx=5, pady=5)
day3Label.grid(row=2, column=0, padx=5, pady=5)
day4Label.grid(row=3, column=0, padx=5, pady=5)
day5Label.grid(row=4, column=0, padx=5, pady=5)
day6Label.grid(row=5, column=0, padx=5, pady=5)
day7Label.grid(row=6, column=0, padx=5, pady=5)

day_1_in.grid(row=0, column=1, padx=5, pady=5)
day_2_in.grid(row=1, column=1, padx=5, pady=5)
day_3_in.grid(row=2, column=1, padx=5, pady=5)
day_4_in.grid(row=3, column=1, padx=5, pady=5)
day_5_in.grid(row=4, column=1, padx=5, pady=5)
day_6_in.grid(row=5, column=1, padx=5, pady=5)
day_7_in.grid(row=6, column=1, padx=5, pady=5)

day_1_out.grid(row=0, column=2, padx=5, pady=5)
day_2_out.grid(row=1, column=2, padx=5, pady=5)
day_3_out.grid(row=2, column=2, padx=5, pady=5)
day_4_out.grid(row=3, column=2, padx=5, pady=5)
day_5_out.grid(row=4, column=2, padx=5, pady=5)
day_6_out.grid(row=5, column=2, padx=5, pady=5)
day_7_out.grid(row=6, column=2, padx=5, pady=5)

button_calculate.grid(row=7, column=1, padx=10, pady=10)
button_save.grid(row=7, column=2, padx=10, pady=10)
button_clear.grid(row=7, column=3, padx=10, pady=10)

my_results.grid(row=0, column=3, padx=10, pady=10, columnspan=2, rowspan=7)

apply_default_values()

root.mainloop()