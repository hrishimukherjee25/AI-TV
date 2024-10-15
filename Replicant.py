import tkinter as tk
from tkinter import scrolledtext

# Function to handle sending messages
def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    if user_message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {user_message}\n")
        chat_window.insert(tk.END, f"Assistant: {get_response(user_message)}\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        user_input.delete("1.0", tk.END)

# Simulate assistant's response
def get_response(user_message):
    return "This is a response from the assistant."

# Create the main window
root = tk.Tk()
root.title("ChatGPT UI Replication")
root.geometry("500x600")

# Create chat window
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create input text box
user_input = tk.Text(root, height=3)
user_input.pack(padx=10, pady=10, fill=tk.X)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
