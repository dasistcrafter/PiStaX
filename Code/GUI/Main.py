from display_sim import SimDisplay
from PIL import ImageFont
import json
import psutil
import datetime

#time config
x = datetime.datetime.now()

font_stats = ImageFont.truetype("arial.ttf",14)
font_time = ImageFont.truetype("arialbd.ttf", 14)

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
    time = x.strftime("%c")
    # Beispielhafte Textanzeige, falls "Time" aktiviert ist
    if data.get("Time") == True:
        display.draw.text((175, 10), x.strftime("%X") , font=font_time, fill="white")

    if data.get("Date") == True:
        display.draw.text((10, 10), x.strftime("%x"), font=font_time, fill="white")

    if data.get("CPU_usage") == True:
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),f"CPU: {psutil.cpu_percent(interval=None)}%",font=font_stats,fill="white")

    if data.get("CPU_temp") == True:
        frequency_all = psutil.cpu_freq(percpu=False)
        frequency_current = frequency_all[17:23]
        stats_shown += 1
        display.draw.text((10,(stats_shown * 20) + 100 ), f"CPU frequency:  {frequency_current}", font=font_stats, fill="white")
        stats_shown += 1
        print(frequency_current)
        print(psutil.cpu_freq(percpu=False))
    
    if data.get("RAM_usage") == True:
        stats_shown += 1
        display.draw.text((10,(stats_shown * 20) + 100 ), "RAM: XX%", font=font_stats, fill="white")
        print(stats_y)
    
    if data.get("Storage_usage") == True:
        stats_shown += 1
        display.draw.text((10,(stats_shown * 20) + 100 ), "Storage: XX %", font=font_stats, fill="white")
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
