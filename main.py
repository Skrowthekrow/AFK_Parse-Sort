import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.scrolledtext import ScrolledText


# function to parse the file and return the sorted data
def parse_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except:
        messagebox.showerror("Error", "Unable to open file.")
        return []

    # initialize a list to hold the cleaned and parsed data
    mil = []
    bil = []

    # loop through each line in the file
    for line in lines:
        # strip leading/trailing whitespace and split the line into two parts
        name, number = line.strip().split(' - ')
        # check the last character of the number to determine its suffix
        if number[-1] == 'B':
            # remove "B", "M", and "-" characters from the number
            number = number.replace('B', '').replace('M', '').replace('-', '')
            # convert the number to an integer or float, depending on its format
            number = int(number)
            bil.append((name, f"{number}B"))
        elif number[-1] == 'M':
            # remove "B", "M", and "-" characters from the number
            number = number.replace('B', '').replace('M', '').replace('-', '')
            # convert the number to an integer or float, depending on its format
            number = int(number)
            mil.append((name, f"{number}M"))
        else:
            # remove "B", "M", and "-" characters from the number
            number = number.replace('B', '').replace('M', '').replace('-', '')
            # convert the number to an integer or float, depending on its format
            number = int(number)
            mil.append((name, f"{number}"))

    # sort the lists in descending order by number
    mil.sort(key=lambda x: (len(x[1]), x[1]), reverse=True)
    bil.sort(key=lambda x: (len(x[1]), x[1]), reverse=True)

    # concatenate the two lists
    sorted_data = bil + mil

    return sorted_data

# function to handle the "Browse" button click event
def browse_file():
    filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
    filename = filedialog.askopenfilename(title="Select a file", filetypes=filetypes)
    if filename:
        # parse the file and display the sorted data in a new window
        sorted_data = parse_file(filename)
        if sorted_data:
            display_data(sorted_data)

# function to display the sorted data in a new window
def display_data(sorted_data):
    top = tk.Toplevel(root)
    top.title("Sorted Data")

    # create a scrolledtext widget to display the data
    st = ScrolledText(top, width=50, height=20)
    st.pack()

    # insert each line of data into the scrolledtext widget
    for name, number in sorted_data:
        st.insert(tk.END, f"{name}: {number}\n")

    # make the scrolledtext widget read-only
    st.configure(state='disabled')

# create the main window
root = tk.Tk()
root.title("File Parser")

# create the "Browse" button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# start the event loop
root.mainloop()