import tkinter as tk
from tkinter import messagebox

#STACK CLASS

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1] if self.items else "Empty"

    def size(self):
        return len(self.items)

    def isempty(self):
        return len(self.items) == 0


stack = Stack()

#FUNCTIONS

def update_display():
    if stack.items:
        stack_box.config(text="\n".join(reversed(stack.items)))
    else:
        stack_box.config(text="STACK EMPTY")


def push_item():
    value = entry.get().strip()

    if value == "":
        messagebox.showwarning("Input Error", "Enter a value first!")
        return

    stack.push(value)

    status_label.config(
        text=f"✓ PUSH Successful | Added '{value}'"
    )

    entry.delete(0, tk.END)
    update_display()


def pop_item():
    value = stack.pop()

    if value is None:
        status_label.config(text="✗ Stack is Empty")
    else:
        status_label.config(
            text=f"✓ POP Successful | Removed '{value}'"
        )

    update_display()


def peek_item():
    status_label.config(
        text=f"Top Element → {stack.peek()}"
    )


def size_item():
    status_label.config(
        text=f"Stack Size → {stack.size()}"
    )


def isempty_item():
    status_label.config(
        text=f"Is Empty → {'Yes' if stack.isempty() else 'No'}"
    )


#WINDOW

root = tk.Tk()
root.title("Stack ADT Simulator")
root.geometry("1400x800")
root.configure(bg="#111827")

#TITLE

title = tk.Label(
    root,
    text="STACK ADT SIMULATOR",
    bg="#111827",
    fg="white",
    font=("Bahnschrift", 28, "bold")
)

title.pack(pady=20)

#INPUT

tk.Label(
    root,
    text="Input Value",
    bg="#111827",
    fg="white",
    font=("Segoe UI", 13, "bold")
).pack()

entry = tk.Entry(
    root,
    width=35,
    justify="center",
    font=("Segoe UI", 16),
    bg="#1F2937",
    fg="white",
    insertbackground="white"
)

entry.pack(pady=10, ipady=8)

#BUTTONS

button_frame = tk.Frame(root, bg="#111827")
button_frame.pack(pady=20)

style = {
    "font": ("Segoe UI", 12, "bold"),
    "width": 15,
    "height": 2,
    "bd": 0
}

tk.Button(
    button_frame,
    text="PUSH",
    bg="mediumseagreen",
    fg="white",
    command=push_item,
    **style
).pack(side="left", padx=21)

tk.Button(
    button_frame,
    text="POP",
    bg="crimson",
    fg="white",
    command=pop_item,
    **style
).pack(side="left", padx=21)

tk.Button(
    button_frame,
    text="PEEK",
    bg="turquoise",
    fg="black",
    command=peek_item,
    **style
).pack(side="left", padx=21)

tk.Button(
    button_frame,
    text="ISEMPTY",
    bg="gold",
    fg="black",
    command=isempty_item,
    **style
).pack(side="left", padx=21)

tk.Button(
    button_frame,
    text="SIZE",
    bg="mediumslateblue",
    fg="white",
    command=size_item,
    **style
).pack(side="left", padx=21)

tk.Button(
    button_frame,
    text="QUIT",
    bg="darkgray",
    fg="white",
    command=root.destroy,
    **style
).pack(side="left", padx=21)

#STACK DISPLAY

stack_frame = tk.Frame(
    root,
    bg="#1F2937",
    relief="solid",
    bd=1
)

stack_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

tk.Label(
    stack_frame,
    text="STACK DISPLAY",
    bg="#1F2937",
    fg="#00D1FF",
    font=("Bahnschrift", 20, "bold")
).pack(pady=15)

stack_box = tk.Label(
    stack_frame,
    text="STACK EMPTY",
    bg="#1F2937",
    fg="white",
    font=("Consolas", 26, "bold"),
    justify="center"
)

stack_box.pack(expand=True)

#OPERATION STATUS

tk.Label(
    root,
    text="OPERATION STATUS",
    bg="#111827",
    fg="#9CA3AF",
    font=("Bahnschrift", 16, "bold")
).pack(pady=(10, 5))

status_label = tk.Label(
    root,
    text="Perform Stack Operations",
    bg="#1F2937",
    fg="white",
    font=("Segoe UI", 13),
    height=4
)

status_label.pack(
    fill="x",
    padx=120,
    pady=(0, 15)
)

update_display()

root.mainloop()
