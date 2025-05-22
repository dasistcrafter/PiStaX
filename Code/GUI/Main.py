from display_sim import SimDisplay
from PIL import ImageFont
import json


font_stats = ImageFont.truetype("arial.ttf", 10)
font_time = ImageFont.truetype("arial.ttf", 10)

# load settings data
with open("settings.json", "r") as f:
    data = json.load(f)

display = SimDisplay()
select = 0  # Ausgewählter Button (0–4)
stats_shown = 0
stats_y = 60

def draw_buttons():
    display.clear("black")

    button_width = 40
    spacing = 6
    total_width = 5 * button_width + 4 * spacing 
    start_x = (240 - total_width) // 2 

    for i in range(5):
        x = start_x + i * (button_width + spacing)
        outline_color = "white"
        line_width = 4 if i == select else 2
        display.draw.rounded_rectangle(
            (x, 30, x + button_width, 70),
            radius=10,
            outline=outline_color,
            width=line_width
        )

    # Zeige die Stats mit an
    show_stats()

    # Display aktualisieren
    display.show()

def show_stats():
    global stats_shown
    stats_shown = 1
    # Beispielhafte Textanzeige, falls "Time" aktiviert ist
    if data.get("Time") == True:
        display.draw.text((195, 10), "MM:HH", font=font_small, fill="white")

    if data.get("Date") == True:
        display.draw.text((10, 10), "DD:MM:YYYY", font=font_small, fill="white")

    if data.get("CPU_usage") == True:
        stats_shown += 1
        display.draw.text((10,(stats_shown * 20) + 100 ), "CPU: XX%", font=font_small, fill="white")
        print(stats_y)

def on_key(event):
    global select
    key = event.keysym

    if key == "Left":
        select = max(0, select - 1)
    elif key == "Right":
        select = min(4, select + 1)
    elif key == "Return":
        print(f"⏎ Button {select + 1} gedrückt!")

    draw_buttons()

# Tasteneingaben aktivieren
display.window.bind("<Key>", on_key)

# Erste Anzeige
draw_buttons()

# Starten
display.mainloop()
