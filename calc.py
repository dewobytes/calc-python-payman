from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1E1E2E")

expression = ""

display = tk.Entry(
    root,
    font=("Arial", 28),
    bg="#313244",
    fg="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=20, ipady=20)

def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    try:
        expression = display.get()

        result = eval(expression, {"__builtins__": {}}, {})

        payment = messagebox.askokcancel(
            "PAYMAN N!",
            "SELESAIKAN PEMBAYARAN KREDIT UNTUK MELIHAT HASIL 💳\n\n"
            "Klik OK Jika sudah membayar."
        )

        if payment:
            display.delete(0, tk.END)
            display.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror(
            "Error",
            "Tidak bisa membagi dengan nol!"
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Perhitungan Kosong/tidak valid!"
        )

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

for row in buttons:
    frame = tk.Frame(root, bg="#1E1E2E")
    frame.pack(expand=True, fill="both", padx=10)

    for value in row:

        if value == "=":
            command = calculate
            color = "#A6E3A1"
            text_color = "#11111B"

        elif value == "C":
            command = clear
            color = "#F38BA8"
            text_color = "#11111B"

        elif value == "⌫":
            command = delete
            color = "#FAB387"
            text_color = "#11111B"

        else:
            command = lambda v=value: click(v)
            color = "#45475A" if value in "+-*/%" else "#313244"
            text_color = "white"

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 17, "bold"),
            bg=color,
            fg=text_color,
            activebackground="#585B70",
            bd=0,
            command=command
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )

root.mainloop()
