#! python3

############ Load the libraries
import math
from math import *
from scipy.stats import t
from tkinter import *
from tkinter import messagebox, Label, Button, Entry, Tk




##################################### BUTTON FUNCTIONS
# What the buttons do: functions
def show_correlation_coefficient_stats():
    # Get the values from the entries in the window
    try:
        correlation_coefficient = float(enter_coefficient.get())
    except:
        correlation_coefficient = ''
    try:
        number_of_samples = int(enter_number_of_samples.get())
    except:
        number_of_samples = ''
    try:
        tails = int(enter_tails.get())
    except:
        tails = ''
    try:
        correlation_type = enter_correlation_type.get()
    except:
        correlation_type = ''
    try:
        level_of_significance = float(enter_level_of_significance.get())
    except:
        level_of_significance = ''
    # Fix the values
    if tails == '':
        tails = 2
    if correlation_type == '':
        correlation_type = 'pearson'
    if level_of_significance == '':
        level_of_significance = 0.05
    # Return the alarm
    if (correlation_coefficient == '' or number_of_samples == ''):
        messagebox.showwarning(title="Error", message="Missing critical values!")
    else:
        ####### Calculation of the Student's t-distribution
        degrees_of_freedom = number_of_samples-2
        if correlation_type == "pearson":
            t_value = correlation_coefficient * sqrt((number_of_samples-2)/(1-correlation_coefficient**2))
            # Calculate the one-tail p-value
            p_value = t.sf(t_value, degrees_of_freedom)
            if tails == 1:
                messagebox.showinfo(title="Correlation p-value", message="The p-value for a %s correlation coefficient (of %s) computed on %s samples is: %s" %(correlation_type, correlation_coefficient, number_of_samples, p_value))
            # Calculate the two-tail p-value
            elif tails == 2:
                p_value = p_value*2
                messagebox.showinfo(title="Correlation p-value", message="The p-value for a %s correlation coefficient (of %s) computed on %s samples is: %s" %(correlation_type, correlation_coefficient, number_of_samples, p_value))
            ###################### Significance
            if p_value <= level_of_significance:
                messagebox.showinfo(title="Significance", message="The calculated correlation coefficient IS statistically significant at a level of significance of %s" %(level_of_significance))
            else:
                messagebox.showinfo(title="Significance", message="The calculated correlation coefficient is NOT statistically significant at a level of significance of %s" %(level_of_significance))




################################################ INPUT
# Root window
root = Tk()
root.title("Correlation coefficient significance")
root.resizable(True,True)
root.wm_minsize(width=450, height=150)
# Labels
coefficient_label = Label(root, text="Correlation coefficient")
number_of_samples_label = Label(root, text="Number of samples")
tails_label = Label(root, text="Tails")
correlation_type_label = Label(root, text="Correlation type")
level_of_significance_label = Label(root, text="Level of significance")
# Label positions
coefficient_label.grid(row=0, column=0)
number_of_samples_label.grid(row=1, column=0)
tails_label.grid(row=2, column=0)
correlation_type_label.grid(row=3, column=0)
level_of_significance_label.grid(row=4, column=0)
# Entry boxes
enter_coefficient = Entry(root)
enter_number_of_samples = Entry(root)
enter_tails = Entry(root)
enter_correlation_type = Entry(root)
enter_level_of_significance = Entry(root)
# Positioning
enter_coefficient.grid(row=0, column=1)
enter_number_of_samples.grid(row=1, column=1)
enter_tails.grid(row=2, column=1)
enter_correlation_type.grid(row=3, column=1)
enter_level_of_significance.grid(row=4, column=1)
# Buttons
Button(root, text='Quit', command=root.destroy).grid(row=5, column=0, sticky=W, pady=4)
Button(root, text='Calculate correlation coefficient significance', command=show_correlation_coefficient_stats).grid(row=5, column=1, sticky=W, pady=4)
root.mainloop()
