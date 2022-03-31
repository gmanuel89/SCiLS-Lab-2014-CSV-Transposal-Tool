#! python3

#################### SCiLS LAB 2014 CSV TRANSPOSAL TOOL ####################

# Program version (Specified by the program writer!!!!)
program_version = "2017.06.14.1"
### Force update (in case something goes wrong after an update, when checking for updates and reading the variable force_update, the script can automatically download the latest working version, even if the rest of the script is corrupted, because it is the first thing that reads)
force_update = False
### GitHub URL where the R file is
github_url = "https://raw.githubusercontent.com/gmanuel89/SCiLS-Lab-2014-CSV-Transposal-Tool/master/SCiLS%20Lab%202014%20CSV%20Transposal%20Tool.py"
### GitHub URL of the program's WIKI
github_wiki_url = "https://github.com/gmanuel89/SCiLS-Lab-2014-CSV-Transposal-Tool"
### Name of the file when downloaded
script_file_name = "SCiLS Lab 2014 CSV Transposal Tool"
# Change log
change_log = "1. New look!"



############################## Load the required libraries (tkinter for the TCLTK GUI)
import tkinter, os, platform, decimal
#from tkinter import *
from tkinter import messagebox, Label, Button, Entry, Tk, filedialog, font, Radiobutton, StringVar



############################## Initialize the output_folder variable
output_folder = os.getcwd()

############################## Initialize the output file type variable
file_type = "csv"

############################## Initialize the separating character variable
separating_character = ","

############################## Initialize the variable which says if to preserve the header
keep_header = True

############################## Initialize the input_file variable
input_file = ""




############################## FUNCTIONS

########## FUNCTION: Check for updates (from my GitHub page) (it just updates the label telling the user if there are updates) (it updates the check for updates value that is called by the label)
def check_for_updates_function():
    # Initialize the variable that displays the version number and the possible updates
    global check_for_updates_value, update_available, online_change_log, online_version_number, online_force_update
    check_for_updates_value = program_version
    # Initialize the version
    online_version_number = None
    ### Initialize the force update
    online_force_update = False
    # Initialize the variable that says if there are updates
    update_available = False
    ### Initialize the change log
    online_change_log = "Bug fixes"
    try:
        # Import the library
        import urllib.request
        # Retrieve the file from GitHub (read the lines: list with lines)
        github_file_lines = urllib.request.urlopen(github_url).readlines()
        # Decode the lines (from bytes to character)
        for l in range(len(github_file_lines)):
            github_file_lines[l] = github_file_lines[l].decode("utf-8")
        # Retrieve the version number
        for line in github_file_lines:
            if line.startswith("program_version = "):
                # Isolate the "variable" value
                online_version_number = line.split("program_version = ")[1]
                # Remove the quotes
                online_version_number = online_version_number.split("\"")[1]
        ### Retrieve the online force update
        for line in github_file_lines:
            if line.startswith("force_update = "):
                # Isolate the "variable" value
                online_force_update = line.split("force_update = ")[1]
                # Split at the \n
                online_force_update = online_force_update.split("\n")[0]
            if online_force_update == "False":
                online_force_update = False
            elif online_force_update == "True":
                online_force_update = True
            elif online_force_update is None:
                online_force_update = False
        ### Retrieve the change log
        for line in github_file_lines:
            if line.startswith("change_log = "):
                # Isolate the "variable" value
                online_change_log = line.split("change_log = ")[1]
                # Remove the quotes
                online_change_log = online_change_log.split("\"")[1]
                # Split at the \n
                online_change_log_split = online_change_log.split("\n")
                # Put it back to the character
                online_change_log = ""
                for o in online_change_log_split:
                    online_change_log = online_change_log + "\n" + o
        # Split the version number in YYYY.MM.DD
        online_version_YYYYMMDDVV = online_version_number.split(".")
        # Compare with the local version
        local_version_YYYYMMDDVV = program_version.split(".")
        ### Check the versions (from year to day)
        if local_version_YYYYMMDDVV[0] < online_version_YYYYMMDDVV[0]:
            update_available = True
        if update_available is False:
            if (local_version_YYYYMMDDVV[0] == online_version_YYYYMMDDVV[0]) and (local_version_YYYYMMDDVV[1] < online_version_YYYYMMDDVV[1]):
                update_available = True
        if update_available is False:
            if (local_version_YYYYMMDDVV[0] == online_version_YYYYMMDDVV[0]) and (local_version_YYYYMMDDVV[1] == online_version_YYYYMMDDVV[1]) and (local_version_YYYYMMDDVV[2] < online_version_YYYYMMDDVV[2]):
                update_available = True
        if update_available is False:
            if (local_version_YYYYMMDDVV[0] == online_version_YYYYMMDDVV[0]) and (local_version_YYYYMMDDVV[1] == online_version_YYYYMMDDVV[1]) and (local_version_YYYYMMDDVV[2] == online_version_YYYYMMDDVV[2]) and (local_version_YYYYMMDDVV[3] < online_version_YYYYMMDDVV[3]):
                update_available = True
        # Return messages
        if online_version_number is None:
            # The version number could not be ckecked due to internet problems
            check_for_updates_value = "Version: %s\nUpdates not checked: connection problems" %(program_version)
        else:
            if update_available is True:
                # The version number could not be ckecked due to internet problems
                check_for_updates_value = "Version: %s\nUpdate available:\n%s" %(program_version, online_version_number)
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
    if update_available is True or online_force_update is True:
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
        messagebox.showinfo(title="Folder selected", message="The updated script file will be downloaded in:\n\n'%s'" %(download_folder))
        try:
            # Import the library
            import urllib.request
            # Download the new file in the working directory
            os.chdir(download_folder)
            urllib.request.urlretrieve (github_url, "%s.py" %(script_file_name))
            file_downloaded = True
        except:
            pass
        if file_downloaded is True:
            Tk().withdraw()
            messagebox.showinfo(title="Updated file retrieved!", message="The update file named\n\n%s\nhas been retrieved and placed in\n\n%s" %(script_file_name, download_folder))
            Tk().withdraw()
            messagebox.showinfo(title="Changelog", message="The updated script contains the following changes:\n\n%s" %(online_change_log))
        else:
            Tk().withdraw()
            messagebox.showinfo(title="Connection problem", message="The updated script file could not be downloaded due to internet connection problems!\n\nManually download the updated script file at:\n\n%s" %(github_url))
    else:
        check_for_updates_value = "Version: %s\nNo updates available" %(program_version)
        Tk().withdraw()
        messagebox.showinfo(title="No updates available", message="No updates available!")




### Downloading forced updates
check_for_updates_function()

if online_force_update is True:
    download_updates_function()










########## FUNCTION: Select where to save the transposed CSV file
def select_output_folder_function():
    Tk().withdraw()
    messagebox.showinfo(title="Folder selection", message="Select where to dump the transposed CSV file(s)")
    # Where to save the GCODE file (escape function environment)
    global output_folder
    tkinter.Tk().withdraw()
    output_folder = filedialog.askdirectory ()
    # Fix the possible non-defined output folder
    if output_folder == "":
        output_folder = os.getcwd()
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title="Folder selected", message="The transposed CSV file(s) will be dumped in '%s'" %(output_folder))











########## FUNCTION: Select the output file format
def select_output_format_function():
    # Escape the function
    global file_type
    global submit_output_format_value_subfunction
    # Define the function which submits the valuento the program
    def submit_output_format_value_subfunction():
        global file_type
        # Extract the values
        file_type = file_type_entry.get()
        # Default
        #if file_type_input == "":
            #file_type = "csv"
        #else:
            #file_type = str(file_type_input)
        # Collapse the GUI Tk window
        of_window.destroy()
    ########## Main window
    of_window = Tk()
    of_window.title("Output format")
    of_window.resizable(False,False)
    # Radio buttons
    file_type_csv = Radiobutton(of_window, text="Comma Separated Values (.csv)", variable=file_type_entry, value="csv", font=entry_font, justify="left")
    file_type_txt = Radiobutton(of_window, text="Text file (.txt)", variable=file_type_entry, value=".txt", font=entry_font, justify="left")
    # Default selection
    file_type_csv.select()
    file_type_txt.deselect()
    # Positioning
    file_type_csv.pack()
    file_type_txt.pack()
    # Submit button
    Button(of_window, text='Submit', font = button_font, command=submit_output_format_value_subfunction).pack()
    # Hold until quit
    of_window.mainloop()












########## FUNCTION: Select the CSV file to be transposed
def select_input_csv_function():
    # Message for selection (open)
    tkinter.Tk().withdraw()
    tkinter.messagebox.showinfo(title="CSV selection", message="Select the CSV file to be transposed")
    # Escape the function
    global input_file
    # Move to the working directory (set)
    os.chdir(output_folder)
    # CSV file selection
    tkinter.Tk().withdraw()
    input_file = tkinter.filedialog.askopenfilename(filetypes=[('CSV files','.csv'),('TXT files','.txt')])
    if input_file != "":
        # Message for selection
        tkinter.Tk().withdraw()
        tkinter.messagebox.showinfo(title="CSV selected", message="The selected CSV file is:\n\n" + input_file)
    else:
        # Message for selection
        tkinter.Tk().withdraw()
        tkinter.messagebox.showinfo(title="No CSV selected", message="No CSV file has been selected!!")









########## FUNCTION: CSV transposal
def csv_transposal_function():
    ### Get the values from the entries
    # Keep header
    keep_header_input = keep_header_entry.get()
    if keep_header_input == "y":
        keep_header = True
    else:
        keep_header = False
    # Output file
    output_file = filename_entry.get()
    # Separating character
    separating_character = separating_character_entry.get()
    # File type
    file_type = file_type_entry.get()
    ###### Transposal script
    if input_file != "":
        ### Open the input file (in a temporary variable f)
        with open(input_file) as f:
            # Read the csv lines
            csv_file_lines = f.readlines()
            # Create the empty lists for m/z and intensity
            csv_mz_column = []
            csv_int_column = []
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
            # Isolate the header from everything else
            csv_mz_column_header = csv_mz_column_split[0]
            csv_mz_column_values = csv_mz_column_split[1:len(csv_mz_column_split)]
            csv_int_column_header = csv_int_column_split[0]
            csv_int_column_values = csv_int_column_split[1:len(csv_int_column_split)]
            # Convert the values in a simple way (from 3e-003 to 0.003)
            for i in range(len(csv_mz_column_values)):
                csv_mz_column_values[i] = str(decimal.Decimal(csv_mz_column_values[i]))
            for i in range(len(csv_int_column_values)):
                csv_int_column_values[i] = str(decimal.Decimal(csv_int_column_values[i]))
        # Try to append the date and time to the filename (so if someone presses the 'Dump file' button without changing the name it does not overwrite it, because there is a different time appended)
        try:
            import time
            current_date = time.strftime("%Y%m%d-%H.%M.%S")
            output_file = output_file + " (" + current_date + ")"
        except:
            pass
        # Add the extension to the file automatically
        if ("." + file_type) not in output_file:
            output_file = str(output_file) + "." + file_type
        # Move to the working directory (set)
        os.chdir(output_folder)
        ### Open the output file (in a temporary variable f)
        with open(output_file, 'w') as f:
            # Create the empty lists for the transposed CSV lines
            t_csv_rows = []
            # Write the transposed file's CSV rows
            if keep_header is True:
                t_csv_rows.append(csv_mz_column_header.strip() + separating_character + csv_int_column_header.strip() + "\n")
            else:
                pass
            for i in range(len(csv_mz_column_values)):
                t_csv_rows.append(csv_mz_column_values[i].strip() + separating_character + csv_int_column_values[i].strip() + "\n")
            # Write the output lines
            for line in t_csv_rows:
                f.writelines(line)
        ### Message for completion
        tkinter.Tk().withdraw()
        tkinter.messagebox.showinfo(title="CSV transposed!!!", message="The CSV file named\n\n%s\n\nhas been succesfully transposed!" %(output_file))
    else:
        ### Message for completion
        tkinter.Tk().withdraw()
        tkinter.messagebox.showinfo(title="No CSV file", message="Select a CSV file to be transposed first!")










########## FUNCTION: Show the iMatrixSpray Method Gcode Generator info
def show_info():
    # Retrieve the system
    system_os = platform.system()
    if system_os == "Linux":
        os.system("xdg-open " + github_wiki_url)
    elif system_os == "Darwin":
        os.system("open " + github_wiki_url)
    elif system_os == "Windows":
        os.system("cmd /c start " + github_wiki_url)










########## FUNCTION: Close the program
def close_program_function():
    # Collapse the GUI Tk window
    window.destroy()
    # Quit the Python session
    quit()





######################################################################






############################## TCL-TK WINDOW

########## Main window
window = Tk()
window.title("SCiLS Lab 2014 CSV Transposal Tool")
window.resizable(False,False)
window.configure(background = "white")
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
        bitstream_charter_title_bold = font.Font(family = "Bitstream Charter", size = title_font_size, weight = "bold")
        bitstream_charter_other_normal = font.Font(family = "Bitstream Charter", size = other_font_size, weight = "normal")
        bitstream_charter_other_bold = font.Font(family = "Bitstream Charter", size = other_font_size, weight = "bold")
        liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
        liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
        liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = bitstream_charter_title_bold
        label_font = bitstream_charter_other_normal
        entry_font = bitstream_charter_other_normal
        button_font = bitstream_charter_other_bold
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
# macOS
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
title_label = Button(window, text="SCiLS Lab 2014\nCSV Transposal Tool", relief = "flat", command = show_info, background = "white", font = title_font)
check_for_updates_label = Label(window, text=check_for_updates_value, font=label_font, background = "white")


# Initialize the radio button variable
file_type_entry = StringVar()
keep_header_entry = StringVar()
separating_character_entry = StringVar()



########## Entry boxes / Radiobuttons (with positioning)
filename_entry = Entry(window, font=entry_font, justify="center")
filename_entry.insert(0,"Transposed CSV file")
### Keep header
keep_header_yes = Radiobutton(window, text="Yes", variable=keep_header_entry, value="y", font=entry_font, justify="left", background = "white")
keep_header_no = Radiobutton(window, text="No", variable=keep_header_entry, value="n", font=entry_font, justify="left", background = "white")
# Default selection
keep_header_yes.select()
keep_header_no.deselect()
### Separating character
separating_character_tab = Radiobutton(window, text="Tab", variable=separating_character_entry, value="\t", font=entry_font, justify="left", background = "white")
separating_character_space = Radiobutton(window, text="Space", variable=separating_character_entry, value=" ", font=entry_font, justify="left", background = "white")
separating_character_comma = Radiobutton(window, text="Comma", variable=separating_character_entry, value=",", font=entry_font, justify="left", background = "white")
separating_character_semicolon = Radiobutton(window, text="Semicolon", variable=separating_character_entry, value=";", font=entry_font, justify="left", background = "white")
# Default selection
separating_character_comma.select()
separating_character_tab.deselect()
separating_character_space.deselect()
separating_character_semicolon.deselect()
### File type
file_type_csv = Radiobutton(window, text="Comma Separated Values (.csv)", variable=file_type_entry, value="csv", font=entry_font, justify="left", background = "white")
file_type_txt = Radiobutton(window, text="Text file (.txt)", variable=file_type_entry, value="txt", font=entry_font, justify="left", background = "white")
# Default selection
file_type_csv.select()
file_type_txt.deselect()


########## Buttons
select_input_button = Button(window, text='IMPORT CSV FILE...', font = button_font, command=select_input_csv_function, background = "white")
separating_character_label = Label(window, text='Choose the separating\ncharacter', font = label_font, background = "white")
keep_header_label = Label(window, text='Choose whether to\nkeep the header', font = label_font, background = "white")
input_file_type_label = Label(window, text='Choose the output\nfile type', font = label_font, background = "white")
quit_button = Button(window, text='QUIT', font = button_font, command=close_program_function, background = "white")
# Dump the file
dump_file_button = Button(window, text='TRANSPOSE CSV\nAND SAVE', font = button_font, command=csv_transposal_function, background = "white")
# Output folder
browse_output_button = Button(window, text="BROWSE OUTPUT FOLDER...", font = button_font, command=select_output_folder_function, background = "white")
# Download updates
download_update_button = Button(window, text="DOWNLOAD\nUPDATE", font = button_font, relief = "raised", command=download_updates_function, background = "white")


########## Positioning
# Labels
title_label.grid(row=0,column=0, padx = 20, pady = 20)
check_for_updates_label.grid(row=0, column=3, padx = 10, pady = 10)
# Entries and Radiobuttons
filename_entry.grid(row=4, column=0, padx = 10, pady = 10)
keep_header_yes.grid(row=3, column=1, padx = 10, pady = 10)
keep_header_no.grid(row=4, column=1, padx = 10, pady = 10)
separating_character_comma.grid(row=3, column=2, padx = 10, pady = 10)
separating_character_tab.grid(row=4, column=2, padx = 10, pady = 10)
separating_character_space.grid(row=5, column=2, padx = 10, pady = 10)
separating_character_semicolon.grid(row=6, column=2, padx = 10, pady = 10)
file_type_csv.grid(row=3, column=3, padx = 10, pady = 10)
file_type_txt.grid(row=4, column=3, padx = 10, pady = 10)
# Buttons
select_input_button.grid(row=3, column=0, padx = 10, pady = 10)
separating_character_label.grid(row=2, column=2, padx = 10, pady = 10)
keep_header_label.grid(row=2, column=1, padx = 10, pady = 10)
input_file_type_label.grid(row=2, column=3, padx = 10, pady = 10)
quit_button.grid(row=6, column=0, padx = 10, pady = 10)
dump_file_button.grid(row=5, column=0, padx = 10, pady = 10)
browse_output_button.grid(row=2, column=0, padx = 10, pady = 10)
download_update_button.grid(row=0, column=2, padx = 10, pady = 10)

# Hold until quit
window.mainloop()
