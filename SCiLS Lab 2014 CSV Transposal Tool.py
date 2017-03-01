#! python3

#################### SCiLS LAB 2014 CSV TRANSPOSAL TOOL ####################

# Program version (Specified by the program writer!!!!)
program_version = "2017.02.28.1"
### GitHub URL where the R file is
github_url = "https://raw.githubusercontent.com/gmanuel89/Public-Python-UNIMIB/master/SCiLS%20Lab%202014%20CSV%20Transposal%20Tool.py"
### Name of the file when downloaded
script_file_name = "SCiLS Lab 2014 CSV Transposal Tool.py"
# Change log
change_log = "1. Added the possibility to choose the separating character"



############################## Load the required libraries (tkinter for the TCLTK GUI)
import tkinter, os, platform
#from tkinter import *
from tkinter import messagebox, Label, Button, Entry, Tk, filedialog, font



############################## Initialize the output_folder variable
output_folder = os.getcwd()







############################## FUNCTIONS

########## FUNCTION: Check for updates (from my GitHub page) (it just updates the label telling the user if there are updates) (it updates the check for updates value that is called by the label)
def check_for_updates_function():
    # Initialize the variable that displays the version number and the possible updates
    global check_for_updates_value, update_available
    check_for_updates_value = program_version
    # Initialize the version
    online_version_number = None
    # Initialize the variable that says if there are updates
    update_available = False
    try:
        # Import the library
        import urllib.request
        # Retrieve the file from GitHub
        github_file = urllib.request.urlopen(github_url).read()
        # String conversion
        github_file_string = str(github_file)
        # Lines
        github_file_lines = github_file_string.split("\\\\n")
        # Get the first line, with the version number
        first_block = github_file_lines[0].split("\\n")
        # Retrieve the version number
        for line in first_block:
            if line.startswith("program_version = "):
                online_version_number = line.split("program_version = ")[1]
                online_version_number = online_version_number.split("\"")[1]
        # Split the version number in YYYY.MM.DD
        online_version_YYYYMMDDVV = online_version_number.split(".")
        # Compare with the local version
        local_version_YYYYMMDDVV = program_version.split(".")
        for v in range(len(local_version_YYYYMMDDVV)):
            if local_version_YYYYMMDDVV[v] < online_version_YYYYMMDDVV[v]:
                update_available = True
                break
        # Return messages
        if online_version_number is None:
            # The version number could not be ckecked due to internet problems
            check_for_updates_value = "Version: %s\nUpdates not checked: connection problems" %(program_version)
        else:
            if update_available is True:
                # The version number could not be ckecked due to internet problems
                check_for_updates_value = "Version: %s\nUpdates available: %s" %(program_version, online_version_number)
            else:
                check_for_updates_value = "Version: %s\nNo updates available" %(program_version)
    # Something went wrong: library not installed, retrieving failed, errors in parsing the version number
    except:
        # Return messages
        if online_version_number is None:
            # The version number could not be ckecked due to internet problems
            check_for_updates_value = "Version: %s\nUpdates not checked: connection problems" %(program_version)









########## FUNCTION: Download updates (from my GitHub page)
def download_updates_function():
    # Initialize the variable that displays the version number
    global check_for_updates_value
    # Download updates only if there are updates available
    if update_available is True:
        # Initialize the variable which says if the file has been downloaded successfully
        file_downloaded = False
        # Choose where to save the updated script
        Tk().withdraw()
        messagebox.showinfo(title="Download folder", message="Select where to save the updated script file")
        download_folder = filedialog.askdirectory ()
        # Fix the possible non-defined output folder
        if download_folder == "":
            download_folder = os.getcwd()
        # Just to confirm...
        Tk().withdraw()
        messagebox.showinfo(title="Folder selected", message="The updated file will be downloaded in:\n\n'%s'" %(download_folder))
        try:
            # Import the library
            import urllib.request
            # Download the new file in the working directory
            os.chdir(download_folder)
            urllib.request.urlretrieve (github_url, script_file_name)
            file_downloaded = True
        except:
            pass
        if file_downloaded is True:
            Tk().withdraw()
            messagebox.showinfo(title="Updated file retrieved!", message="The update file named\n%s\nhas been retrieved and placed in\n%s" %(script_file_name, download_folder))
        else:
            Tk().withdraw()
            messagebox.showinfo(title="Connection problem", message="The updated script file could not be downloaded due to internet connection problems!\n\nManually download the updated script file at:\n\n%s" %(github_url))
    else:
        check_for_updates_value = "Version: %s\nNo updates available" %(program_version)
        Tk().withdraw()
        messagebox.showinfo(title="No updates available", message="No updates available!")











########## FUNCTION: Select where to save the GCODE method file
def select_output_folder_function():
    Tk().withdraw()
    messagebox.showinfo(title="Folder selection", message="Select where to dump the transposed CSV file(s)")
    # Where to save the GCODE file (escape function environment)
    global output_folder
    output_folder = filedialog.askdirectory ()
    # Fix the possible non-defined output folder
    if output_folder == "":
        output_folder = os.getcwd()
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title="Folder selected", message="The transposed CSV file(s) will be dumped in '%s'" %(output_folder))










########## FUNCTION: Select where to save the GCODE method file
def select_input_csv_function():
    # Message for selection (open)
    tkinter.Tk().withdraw()
    tkinter.messagebox.showinfo(title="CSV selection", message="Select the CSV file to be transposed")
    # Escape the function
    global input_file
    # CSV file selection
    tkinter.Tk().withdraw()
    input_file = tkinter.filedialog.askopenfilename(filetypes=[('CSV files','.csv'),('TXT files','.txt')])
    # Message for selection
    tkinter.Tk().withdraw()
    tkinter.messagebox.showinfo(title="CSV selected", message="The selected CSV file is:\n\n" + input_file)










########## FUNCTION: CSV transposal
def csv_transposal_function():
    ###### Transposal script
    ### Open the input file (in a temporary variable f)
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
    # Move to the working directory (set)
    os.chdir(output_folder)
    # Get the filename from the GUI entry
    output_file = filename_entry.get()
    # Add the extension to the file automatically
    if ".csv" not in output_file:
        output_file = str(output_file) + ".csv"
    ### Open the output file (in a temporary variable f)
    with open(output_file, 'w') as f:
        # Create the empty lists for the transposed CSV lines
        t_csv_rows = []
        # Write the transposed file's CSV rows
        for i in range(len(csv_mz_column_split)):
            t_csv_rows.append(csv_mz_column_split[i].strip() + "," + csv_int_column_split[i].strip() + "\n")
        # Write the output lines
        for line in t_csv_rows:
            f.writelines(line)
    ### Message for completion
    tkinter.Tk().withdraw()
    tkinter.messagebox.showinfo(title="CSV transposed!!!", message="The CSV file has been succesfully transposed!")









########## FUNCTION: Close the program
def close_program_function():
    # Collapse the GUI Tk window
    window.destroy
    # Quit the Python session
    quit()





######################################################################






############################## TCL-TK WINDOW
##### Check for updates
check_for_updates_function()

########## Main window
window = Tk()
window.title("SCiLS Lab 2014 CSV Transposal Tool")
window.resizable(False,False)
#window.wm_minsize(width=550, height=600)

# Get the resolution of the screen (to adjust the font size accordingly)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

##### Fonts
### Store the fonts in a variable for faster editing
# Get system info (Platform - Release - Version (- Linux Distro))
system_os = platform.system()
os_release = platform.release()
os_version = platform.version()
# Default sizes (determined on a 1680x1050 screen) (in order to make them adjust to the size screen, the screen resolution should be retrieved)
#title_font_size = 24
#other_font_size = 11
# Determine the font size according to the resolution
total_number_of_pixels = screen_width * screen_height
# Determine the scaling factor (according to a complex formula)
scaling_factor_title_font = float((0.03611 * total_number_of_pixels) + 9803.1254)
scaling_factor_other_font = float((0.07757 * total_number_of_pixels) + 23529.8386)
title_font_size = int(round(total_number_of_pixels / scaling_factor_title_font))
other_font_size = int(round(total_number_of_pixels / scaling_factor_other_font))
# Windows
if system_os == "Windows":
    # Define the fonts
    garamond_title_bold = font.Font(family = "Garamond", size = title_font_size, weight = "bold")
    garamond_other_normal = font.Font(family = "Garamond", size = other_font_size, weight = "normal")
    arial_title_bold = font.Font(family = "Arial", size = title_font_size, weight = "bold")
    arial_other_normal = font.Font(family = "Arial", size = other_font_size, weight = "normal")
    trebuchet_title_bold = font.Font(family = "Trebuchet MS", size = title_font_size, weight = "bold")
    trebuchet_other_normal = font.Font(family = "Trebuchet MS", size = other_font_size, weight = "normal")
    trebuchet_other_bold = font.Font(family = "Trebuchet MS", size = other_font_size, weight = "bold")
    # Use them in the GUI
    title_font = trebuchet_title_bold
    label_font = trebuchet_other_normal
    entry_font = trebuchet_other_normal
    button_font = trebuchet_other_bold
# Linux
elif system_os == "Linux":
    # Retrieve the linux distribution
    linux_distro = platform.linux_distribution()
    # Ubuntu
    if "Ubuntu" in linux_distro or "Ubuntu" in os_version:
        # Define the fonts
        ubuntu_title_bold = font.Font(family = "Ubuntu", size = title_font_size, weight = "bold")
        ubuntu_other_normal = font.Font(family = "Ubuntu", size = other_font_size, weight = "normal")
        ubuntu_other_bold = font.Font(family = "Ubuntu", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = ubuntu_title_bold
        label_font = ubuntu_other_normal
        entry_font = ubuntu_other_normal
        button_font = ubuntu_other_bold
    # Fedora
    elif "Fedora" in linux_distro or "Fedora" in os_version:
        # Define the fonts
        liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
        liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
        liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
        cantarell_title_bold = font.Font(family = "Cantarell", size = title_font_size, weight = "bold")
        cantarell_other_normal = font.Font(family = "Cantarell", size = other_font_size, weight = "normal")
        cantarell_other_bold = font.Font(family = "Cantarell", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = liberation_title_bold
        label_font = liberation_other_normal
        entry_font = liberation_other_normal
        button_font = liberation_other_bold
    # Other linux distros
    else:
        # Define the fonts
        liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
        liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
        liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = liberation_title_bold
        label_font = liberation_other_normal
        entry_font = liberation_other_normal
        button_font = liberation_other_bold
elif system_os == "Mac":
    # Define the fonts
    helvetica_title_bold = font.Font(family = "Helvetica", size = title_font_size, weight = "bold")
    helvetica_other_normal = font.Font(family = "Helvetica", size = other_font_size, weight = "normal")
    helvetica_other_bold = font.Font(family = "Helvetica", size = other_font_size, weight = "bold")
    # Use them in the GUI
    title_font = helvetica_title_bold
    label_font = helvetica_other_normal
    entry_font = helvetica_other_normal
    button_font = helvetica_other_bold
else:
    # Define the fonts
    courier_title_bold = font.Font(family = "Courier New", size = title_font_size, weight = "bold")
    courier_other_normal = font.Font(family = "Courier New", size = other_font_size, weight = "normal")
    courier_other_bold = font.Font(family = "Courier New", size = other_font_size, weight = "bold")
    # Use them in the GUI
    title_font = courier_title_bold
    label_font = courier_other_normal
    entry_font = courier_other_normal
    button_font = courier_other_bold
#font.families(root = window)



########## Labels (with grid positioning)
title_label = Label(window, text="SCiLS Lab 2014 CSV Transposal Tool", font=title_font).grid(row=0,column=1)
check_for_updates_label = Label(window, text=check_for_updates_value, font=label_font).grid(row=1, column=2)
label_1 = Label(window, text="1. Select the input CSV file", font=label_font).grid(row=2, column=0)
label_2 = Label(window, text="2. Browse where to save the\ntransposed CSV file", font=label_font).grid(row=3, column=0)
label_3 = Label(window, text="3. Select the name of the\ntransposed CSV file", font=label_font).grid(row=4, column=0)
label_4 = Label(window, text="4. Transpose the CSV file", font=label_font).grid(row=5, column=0)
label_5 = Label(window, text="5. Quit or restart from 1", font=label_font).grid(row=6, column=0)

########## Entry boxes / Radiobuttons (with positioning)
filename_entry = Entry(window, font=entry_font, justify="center")
filename_entry.insert(0,"Transposed CSV file")
filename_entry.grid(row=4, column=1)

########## Buttons (with positioning)
Button(window, text='Input CSV file...', font = button_font, command=select_input_csv_function).grid(row=2, column=1)
Button(window, text='Quit', font = button_font, command=close_program_function).grid(row=6, column=1)
# Dump the file
Button(window, text='Transpose CSV and Save', font = button_font, command=csv_transposal_function).grid(row=5, column=1)
# Output folder
Button(window, text="Browse output folder", font = button_font, command=select_output_folder_function).grid(row=3, column=1)
# Download updates
Button(window, text="Download updates", relief = "raised", command=download_updates_function).grid(row=1, column=1)
# Hold until quit
window.mainloop()
