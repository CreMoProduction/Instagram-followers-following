import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
folder = filedialog.askdirectory() # Open a dialog to select a folder

file_name1= "followers"
file_name2= "following"
file_path1 = folder+"/"+file_name1+".txt"
file_path2 = folder+"/"+file_name2+".txt"
# Open the file in read mode
def import_txt(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        file_contents = file.read()
        return(file_contents)

followers =import_txt(file_path1)
followers = re.findall(r'href="/([^/]+)/', followers)
following= import_txt(file_path2)
following = re.findall(r'href="/([^/]+)/', following)

set1 = set(followers) # Convert the lists to sets
set2 = set(following)
unique_items = set2 - set1 # Find the unique items in list2

followers= str(followers)
following= str(following)
unique_items =str(unique_items)
# Print the extracted content
print("Followers: "+followers)
print("following: "+following)
print("They are not following you: "+unique_items)
