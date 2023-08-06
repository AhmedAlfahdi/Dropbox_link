# install pyperclip module using pip install pyperclip

import pyperclip

def replace_dropbox_url(url):
    # Replace www.dropbox.com with dl.dropboxusercontent.com
    new_url = url.replace("www.dropbox.com", "dldropboxusercontent.com")
    
    # Remove ?dl=0 from the end of the URL
    if new_url.endswith("?dl=0"):
        new_url = new_url[:-5]  # Remove the last 5 characters (?dl=0)
    
    return new_url

# Loop until the user enters "exit"
while True:
    # User input and output
    original_url = input("Enter the URL (or 'exit' to quit): ")
    
    if original_url == "exit":
        break  # Exit the loop
    
    modified_url = replace_dropbox_url(original_url)
    pyperclip.copy(modified_url)  # Copy the modified URL to clipboard
    print(modified_url)
    print("The modified URL has been copied to clipboard.")