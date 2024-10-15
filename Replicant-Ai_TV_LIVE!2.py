import tkinter as tk
import time

# Function to simulate AI TV LIVE! transforming shapes
def ai_tv_live():
    shapes = ["Sword", "Dog", "House"]
    for shape in shapes:
        canvas.delete("all")  # Clear the previous shape
        if shape == "Sword":
            draw_sword()
        elif shape == "Dog":
            draw_dog()
        elif shape == "House":
            draw_house()
        
        tv_window.config(state=tk.NORMAL)
        tv_window.insert(tk.END, f"AI TV LIVE! Transforming to {shape}...\n")
        tv_window.config(state=tk.DISABLED)
        tv_window.yview(tk.END)
        
        root.update()  # Update the window after each change
        time.sleep(2)  # Simulate the transformation with a delay

    tv_window.config(state=tk.NORMAL)
    tv_window.insert(tk.END, "Transformation complete!\n")
    tv_window.config(state=tk.DISABLED)
    tv_window.yview(tk.END)

# Function to draw a sword on the canvas
def draw_sword():
    canvas.create_rectangle(140, 50, 160, 200, fill="gray")  # Sword blade
    canvas.create_rectangle(120, 180, 180, 200, fill="brown")  # Sword hilt

# Function to draw a simple dog (represented as an oval here)
def draw_dog():
    canvas.create_oval(100, 100, 300, 200, fill="lightgray")  # Body
    canvas.create_oval(70, 90, 130, 140, fill="gray")  # Head

# Function to draw a house on the canvas
def draw_house():
    canvas.create_rectangle(100, 150, 250, 300, fill="lightblue")  # House base
    canvas.create_polygon(100, 150, 175, 80, 250, 150, fill="brown")  # Roof

# Create the main window
root = tk.Tk()
root.title("ChatGPT UI with AI TV LIVE!")
root.geometry("1000x600")

# Create a frame for chat and AI TV LIVE!
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Chat section
chat_frame = tk.Frame(main_frame)
chat_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create chat window
chat_window = tk.Text(chat_frame, state=tk.DISABLED, wrap=tk.WORD, height=15)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create input text box
user_input = tk.Text(chat_frame, height=3)
user_input.pack(padx=10, pady=10, fill=tk.X)

# Create a send button
send_button = tk.Button(chat_frame, text="Send")
send_button.pack(padx=10, pady=5)

# AI TV LIVE! section
tv_frame = tk.Frame(main_frame)
tv_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create AI TV LIVE! window for messages
tv_window = tk.Text(tv_frame, state=tk.DISABLED, wrap=tk.WORD, height=5)
tv_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a canvas for AI TV LIVE! graphical content
canvas = tk.Canvas(tv_frame, width=400, height=400, bg="white")
canvas.pack(padx=10, pady=10)

# Create a button for AI TV LIVE! action
ai_tv_button = tk.Button(tv_frame, text="Start AI TV LIVE!", command=ai_tv_live)
ai_tv_button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
