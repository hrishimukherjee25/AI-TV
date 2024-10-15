import tkinter as tk
from tkinter import scrolledtext
import time

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

# Function to simulate AI TV LIVE! transforming shapes
def ai_tv_live():
    shapes = ["Sword", "Dog", "House"]
    for shape in shapes:
        tv_window.config(state=tk.NORMAL)
        tv_window.insert(tk.END, f"AI TV LIVE! Transforming to {shape}...\n")
        tv_window.config(state=tk.DISABLED)
        tv_window.yview(tk.END)
        root.update()  # Update the window after each change
        time.sleep(2)  # Simulate the transformation with a delay

    # After transformation, display a finished message
    tv_window.config(state=tk.NORMAL)
    tv_window.insert(tk.END, "Transformation complete!\n")
    tv_window.config(state=tk.DISABLED)
    tv_window.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatGPT UI with AI TV LIVE!")
root.geometry("800x600")

# Create a frame for chat and AI TV LIVE!
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Chat section
chat_frame = tk.Frame(main_frame)
chat_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create chat window
chat_window = scrolledtext.ScrolledText(chat_frame, state=tk.DISABLED, wrap=tk.WORD, height=15)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create input text box
user_input = tk.Text(chat_frame, height=3)
user_input.pack(padx=10, pady=10, fill=tk.X)

# Create a send button
send_button = tk.Button(chat_frame, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

# AI TV LIVE! section
tv_frame = tk.Frame(main_frame)
tv_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create AI TV LIVE! window
tv_window = scrolledtext.ScrolledText(tv_frame, state=tk.DISABLED, wrap=tk.WORD, height=15)
tv_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a button for AI TV LIVE! action
ai_tv_button = tk.Button(tv_frame, text="Start AI TV LIVE!", command=ai_tv_live)
ai_tv_button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
