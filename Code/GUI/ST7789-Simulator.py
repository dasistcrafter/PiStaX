# display_sim.py
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

WIDTH, HEIGHT = 240, 240

class SimDisplay:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ST7789 Simulation")
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.resizable(False, False)

        self.img = Image.new("RGB", (WIDTH, HEIGHT), "black")
        self.draw = ImageDraw.Draw(self.img)
        self.tk_img = ImageTk.PhotoImage(self.img)

        self.label = tk.Label(self.window, image=self.tk_img)
        self.label.pack()

    def show(self):
        # Aktualisiert das angezeigte Bild
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.label.config(image=self.tk_img)
        self.label.image = self.tk_img

    def clear(self, color="black"):
        # Bildschirm leeren
        self.img = Image.new("RGB", (WIDTH, HEIGHT), color)
        self.draw = ImageDraw.Draw(self.img)

    def mainloop(self):
        self.window.mainloop()
