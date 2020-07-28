import tkinter as tk
from tkinter import ttk
n = ["X", "O"]
i = 0


def start_print(event):
    global i;
    if i == 0:
        app.title("Zero move")
        i = 1
    elif i == 1:
        app.title("Cross stroke")
        i = 0


app = tk.Tk()
app.title("Cross stroke")
entry_1 = ttk.Entry(app, width=6)
entry_1.grid(row=1, column=0)
entry_1.bind("<Button-1>", start_print)
entry_2 = ttk.Entry(app, width=6)
entry_2.grid(row=1, column=1)
entry_2.bind("<Button-1>", start_print)
entry_3 = ttk.Entry(app, width=6)
entry_3.grid(row=1, column=2)
entry_3.bind("<Button-1>", start_print)
entry_4 = ttk.Entry(app, width=6)
entry_4.grid(row=2, column=0)
entry_4.bind("<Button-1>", start_print)
entry_5 = ttk.Entry(app, width=6)
entry_5.grid(row=2, column=1)
entry_5.bind("<Button-1>", start_print)
entry_6 = ttk.Entry(app, width=6)
entry_6.grid(row=2, column=2)
entry_6.bind("<Button-1>", start_print)
entry_7 = ttk.Entry(app, width=6)
entry_7.grid(row=3, column=0)
entry_7.bind("<Button-1>", start_print)
entry_8 = ttk.Entry(app, width=6)
entry_8.grid(row=3, column=1)
entry_8.bind("<Button-1>", start_print)
entry_9 = ttk.Entry(app, width=6)
entry_9.grid(row=3, column=2)
entry_9.bind("<Button-1>", start_print)


app.minsize(width=50, height=50)
app.mainloop()