# import libraries
import hashlib
import tkinter as tk
from tkinter import messagebox

# Dictionary to store the long URLs and their corresponding short URLs
url_mapping = {}

# Function to generate short URL
def generate_short_url():
    long_url = entry_long_url.get()
    
    if long_url == "":
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    
    # Generate a short URL using hashlib (MD5)
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:6]
    
    # Store the URL mapping
    url_mapping[short_url] = long_url
    
    # Display the short URL in the GUI
    entry_short_url.delete(0, tk.END)  # Clear previous entry
    entry_short_url.insert(0, short_url)

# Function to retrieve the original long URL from the short URL
def retrieve_long_url():
    short_url = entry_short_url.get()
    
    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        messagebox.showinfo("Long URL", f"The original URL is:\n{long_url}")
    else:
        messagebox.showerror("Error", "Short URL not found!")

#Function to refresh the input
def refresh_fields():
    entry_long_url.delete(0, tk.END) # Clear the long url input field
    entry_short_url.delete(0, tk.END) # Clear the short url input field

# Creating the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x400")
root.configure(bg="#3498db")  # Set a nice background color

# Set window icon (favicon-like)
icon = tk.PhotoImage(file='favicon.PNG')  
root.iconphoto(False, icon)


# Label for Long URL input
label_long_url = tk.Label(root, text="Enter Long URL:", font=("Arial", 12))
label_long_url.pack(pady=10)

# Entry for Long URL
entry_long_url = tk.Entry(root, width=50)
entry_long_url.pack(pady=5)

# Button to generate short URL
button_generate = tk.Button(root, text="Generate Short URL",font=("Arial", 18), command=generate_short_url)
button_generate.pack(pady=10)

# Label for Short URL display
label_short_url = tk.Label(root, text="Short URL:", font=("Arial", 12))
label_short_url.pack(pady=5)

# Entry for Short URL display (read-only)
entry_short_url = tk.Entry(root, width=50)
entry_short_url.pack(pady=5)

# Button to retrieve long URL from short URL
button_retrieve = tk.Button(root, text="Retrieve Long URL", font=("Arial", 18),  command=retrieve_long_url)
button_retrieve.pack(pady=10,)

# Button to retrieve long URL from short URL
button_refresh = tk.Button(root, text="Refresh", font=("Arial", 18),  command=refresh_fields)
button_refresh.pack(pady=10,)

# Start the GUI event loop
root.mainloop()
