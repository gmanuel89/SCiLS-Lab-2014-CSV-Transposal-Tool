#! python3

#################### SCiLS LAB 2014 CSV TRANSPOSAL TOOL ####################

# Program version (Specified by the program writer!!!!)
program_version = "2017.02.28.1"
### GitHub URL where the R file is
#github_url = "https://raw.githubusercontent.com/gmanuel89/iMatrixSpray/master/iMatrixSpray%20Method%20Gcode%20Generator.py"
### Name of the file when downloaded
script_file_name = "SCiLS Lab 2014 CSV Transposal Tool.py"



################## CSV TRANSPOSAL

## CSV LIKE THIS:
# XXXXX
# XXXX
# XXXXXX
# XXXX
#
# RESULT
# XXXX
# XXXX
# XXXX
# XXXX
#  X X
#  X

#### Import the libraries
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import csv

# Message for selection (open)
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="CSV selection", message="Select the CSV file to be transposed")

# CSV file selection
tkinter.Tk().withdraw()
input_file = tkinter.filedialog.askopenfilename(filetypes=[('CSV files','.csv'),('TXT files','.txt')])
print(input_file)

# Message for selection
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="CSV selected", message="The selected CSV file is:\n\n" + input_file)

# Message for selection (save)
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="CSV selection", message="Select where to save the transposed CSV file")

# Where to save the CSV file
tkinter.Tk().withdraw()
output_file = tkinter.filedialog.asksaveasfilename (defaultextension='.csv', filetypes=[('CSV files','.csv'),('TXT files','.txt')])

# Message for selection (save)
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="CSV selected", message="The transposed CSV file will be:\n\n" + output_file)


############################################# Transposal script
# Open the input file (in a temporary variable f)
with open(input_file) as f:
    # Read the csv lines
    csv_file_lines = f.readlines()
    # Create the empty lists for m/z and intensity
    csv_mz_column = None
    csv_int_column = None
    # Scroll the lines of the CSV file...
    for line in csv_file_lines:
        # Discard the non-informative lines (keep only the m/z and the intensities lines)
        if line.startswith("m/z"):
            # Add the values in the row to the vector that will become the column
            csv_mz_column = line
        if line.startswith("intensities"):
            # Add the values in the row to the vector that will become the column
            csv_int_column = line
    # Split the lines at the comma
    csv_mz_column_split = csv_mz_column.split(",")
    csv_int_column_split = csv_int_column.split(",")

# Open the output file (in a temporary variable f)
with open(output_file, 'w') as f:
    # Create the empty lists for the transposed CSV lines
    t_csv_rows = []
    # Write the transposed file's CSV rows
    for i in range(len(csv_mz_column_split)):
        t_csv_rows.append(csv_mz_column_split[i].strip() + "," + csv_int_column_split[i].strip() + "\n")
    # Write the output lines
    for line in t_csv_rows:
        f.writelines(line)


# Message for completion
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="CSV transposed!!!", message="The CSV file has been succesfully transposed")
