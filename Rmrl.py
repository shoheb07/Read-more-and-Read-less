import tkinter as tk

# Full text
full_text = """Python is a powerful programming language used for web development,
data science, artificial intelligence, automation, and many other applications.
It is known for its simple syntax and readability, making it beginner friendly."""

# Short preview
short_text = full_text[:80] + "..."

expanded = False

def toggle_text():
    global expanded
    if expanded:
        label.config(text=short_text)
        button.config(text="Read More")
        expanded = False
    else:
        label.config(text=full_text)
        button.config(text="Read Less")
        expanded = True

# Create window
root = tk.Tk()
root.title("Read More / Read Less Example")
root.geometry("400x200")

label = tk.Label(root, text=short_text, wraplength=350, justify="left")
label.pack(pady=20)

button = tk.Button(root, text="Read More", command=toggle_text)
button.pack()

root.mainloop()
