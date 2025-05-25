from display_sim import SimDisplay
from PIL import ImageFont
import json
import psutil
import datetime

# time config
font_stats = ImageFont.truetype("arial.ttf", 14)
font_time = ImageFont.truetype("arialbd.ttf", 14)

# load settings data
with open("settings.json", "r") as f:
    data = json.load(f)

display = SimDisplay()
select = 0  # Ausgewählter Button (0–4)
stats_shown = 0

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

    # Show the stats
    show_stats()

    # Update display
    display.show()

def show_stats():
    global stats_shown
    stats_shown = 1
    now = datetime.datetime.now()

    # Example text output, if "Time" is enabled
    if data.get("Time") == True:
        display.draw.text((175, 10), now.strftime("%X"), font=font_time, fill="white")

    if data.get("Date") == True:
        display.draw.text((10, 10), now.strftime("%x"), font=font_time, fill="white")

    if data.get("CPU_usage") == True:
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"CPU: {psutil.cpu_percent(interval=None)}%",
                          font=font_stats, fill="white")

    if data.get("CPU_temp") == True:
        freq = psutil.cpu_freq(percpu=False)
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"CPU frequency: {freq.current:.1f} MHz",
                          font=font_stats, fill="white")

    if data.get("RAM_usage") == True:
        ram = psutil.virtual_memory()
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"RAM: {ram.percent}%",
                          font=font_stats, fill="white")

    if data.get("Storage_usage") == True:
        disk = psutil.disk_usage('/')
        stats_shown += 1
        display.draw.text((10, (stats_shown * 20) + 100),
                          f"Storage: {disk.percent}%",
                          font=font_stats, fill="white")

def show_weather():
    #weather will come soon
def show_location():
    #location will come soon


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

# Bind key events
display.window.bind("<Key>", on_key)

# First draw
draw_buttons()

# Automatic redraw loop
def update_loop():
    draw_buttons()
    display.window.after(1000, update_loop)

update_loop()
display.mainloop()