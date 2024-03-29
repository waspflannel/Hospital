import tkinter as tk

class Gui:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Layout")

        self.canvas = tk.Canvas(master, width=600, height=400, bg='white')
        self.canvas.pack()

        # Create rooms
        self.canvas.create_rectangle(50, 50, 200, 150, fill='lightblue', outline='black')
        self.canvas.create_text(125, 100, text="Doctor Room", font=('Helvetica', 10, 'bold'))

        self.canvas.create_rectangle(250, 50, 400, 150, fill='lightgreen', outline='black')
        self.canvas.create_text(325, 100, text="Waiting Room", font=('Helvetica', 10, 'bold'))

        self.canvas.create_rectangle(450, 50, 600, 150, fill='lightcoral', outline='black')
        self.canvas.create_text(525, 100, text="Operating Room", font=('Helvetica', 10, 'bold'))

        self.canvas.create_rectangle(50, 200, 200, 300, fill='lightyellow', outline='black')
        self.canvas.create_text(125, 250, text="Patient Room 1", font=('Helvetica', 10, 'bold'))

        self.canvas.create_rectangle(250, 200, 400, 300, fill='lightyellow', outline='black')
        self.canvas.create_text(325, 250, text="Patient Room 2", font=('Helvetica', 10, 'bold'))

        self.canvas.create_rectangle(450, 200, 600, 300, fill='lightyellow', outline='black')
        self.canvas.create_text(525, 250, text="Patient Room 3", font=('Helvetica', 10, 'bold'))

